import logging
import concurrent.futures
from typing import Dict, List, Optional, Any

# Import smolagents tools
from smolagents.tools import tool

# Import base classes
from .base import BaseAgent, CachingMixin, ValidationMixin
from .tools.shared import DatabaseTools
from ..validation.business_validator import BusinessValidator
from ..validation.tsql_validator import TSQLValidator

logger = logging.getLogger(__name__)

class NL2SQLAgent(BaseAgent, CachingMixin, ValidationMixin):
    """Streamlined NL2SQL Agent with consistent dictionary returns."""
    
    def __init__(self, database_tools: DatabaseTools, shared_llm_model=None):
        # Initialize mixins
        CachingMixin.__init__(self, cache_size=50)
        ValidationMixin.__init__(self)
        
        self.database_tools = database_tools
        
        # Initialize base agent with unified database tools
        super().__init__(
            shared_llm_model=shared_llm_model,
            additional_imports=['json'],
            agent_name="NL2SQL Agent",
            database_tools=self.database_tools
        )

    def _get_schema_depth(self, user_query: str) -> int:
        """Determine how many table schemas to fetch based on query complexity."""
        query_lower = user_query.lower()
        
        # Signals of increasing complexity
        join_signals = ['join', 'together with', 'related', 'linked', 'combined', 
                        'and their', 'with their', 'along with', 'including their']
        multi_signals = ['compare', 'versus', 'vs', 'difference between', 'both']
        aggregate_signals = ['per', 'each', 'breakdown', 'distribution across', 'group by']
        
        score = 2  # default top 2
        
        if any(word in query_lower for word in join_signals):
            score += 1
        if any(word in query_lower for word in multi_signals):
            score += 1
        if any(word in query_lower for word in aggregate_signals):
            score += 1
        
        return min(score, 4)  # cap at 4    

    def _setup_agent_components(self):
        """Setup agent-specific components."""
        self.business_validator = BusinessValidator()
        self.tsql_validator = TSQLValidator()
        
        # Add validators to mixin
        self.add_validator("syntax", self.tsql_validator.validate_syntax)
        self.add_validator("security", self.tsql_validator.validate_security)
        self.add_validator("performance", self.tsql_validator.check_performance_patterns)
    
    def _setup_tools(self):
        """Setup essential NL2SQL tools."""
        self.tools = []
        
        # Database tools will be integrated automatically by BaseAgent
        # Unified database tools include: get_table_schema_unified_tool, get_all_tables_unified_tool, get_relationships_unified_tool
        
        @tool
        def execute_query_and_return_results(query: str, max_rows: int = 100) -> Dict:
            """Execute query and return results.
            
            Args:
                query: The SQL query to execute.
                max_rows: Maximum number of rows to return.
                
            Returns:
                Dictionary with query execution results and sample data.
            """
            try:
                result = self.database_tools.execute_query_safe(query, max_rows)
                
                if not result.get("success"):
                    return result
                
                rows = result.get("rows", [])
                columns = result.get("columns", [])
                
                return {
                    "success": True,
                    "total_rows": len(rows),
                    "returned_rows": len(rows),
                    "truncated": len(rows) >= max_rows,
                    "sample_data": self._create_sample_summary(rows, columns)
                }
                
            except Exception as e:
                logger.error(f"Query execution failed: {e}")
                return {"success": False, "error": str(e)}
        
        # Add final answer tool for SQL response
        @tool
        def final_answer(sql_query: str) -> Dict[str, Any]:
            """Return the final SQL answer.
            
            Args:
                sql_query: The final SQL query to return.
                
            Returns:
                Dictionary with the final SQL query and success status.
            """
            try:
                return {
                    "success": True,
                    "final_sql": sql_query.strip(),
                    "message": "Final SQL query generated"
                }
            except Exception as e:
                return {"success": False, "error": str(e)}
        
        self.tools.extend([
            execute_query_and_return_results,
            final_answer
        ])
    
    def generate_sql_optimized(self, user_query: str, business_context: Dict, entity_context: Dict) -> Dict[str, Any]:
        """Optimized SQL generation with parallel validation."""
        logger.info(f"Starting SQL generation for query: {user_query}")
        try:
            if not isinstance(business_context, dict) or not isinstance(entity_context, dict):
                logger.error("Business context and entity context must be dictionaries")
                return {
                    "success": False,
                    "error": "Business context and entity context must be dictionaries",
                    "generated_sql": "",
                    "is_valid": False
                }
            
            # Build prompt
            prompt = self._build_query_prompt(user_query, business_context, entity_context)
            logger.info(f"Built prompt for SQL generation")
            
            # Generate SQL
            response = self.agent.run(prompt)
            generated_sql = self._extract_sql_from_response(response)
            logger.info(f"Extracted SQL: {generated_sql[:100]}...")
            
            if not generated_sql:
                logger.error("No valid SQL generated")
                return {
                    "success": False,
                    "error": "No valid SQL generated",
                    "generated_sql": "",
                    "is_valid": False
                }
            
            # Check cache
            cache_key = self._get_cache_key(f"{generated_sql}:{hash(str(business_context))}")
            cached_validation = self._get_cached_result(cache_key)
            
            if cached_validation:
                logger.info("Using cached validation results")
                return self._format_response_with_cache(generated_sql, cached_validation)
            
            # Parallel validation and execution
            logger.info("Starting parallel validation")
            return self._execute_parallel_validation(generated_sql, business_context)
            
        except Exception as e:
            logger.error(f"SQL generation failed: {e}")
            return {
                "success": False,
                "error": str(e),
                "generated_sql": "",
                "is_valid": False
            }
    
    def _execute_parallel_validation(self, sql: str, business_context: Dict) -> Dict[str, Any]:
        """Execute parallel validation and query execution."""
        logger.info(f"Starting parallel validation for SQL: {sql[:100]}...")
        
        with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
            # Submit validation tasks
            futures = {
                "syntax": executor.submit(self.validate, sql, "syntax"),
                "business": executor.submit(self._check_business_compliance, sql, business_context),
                "security": executor.submit(self.validate, sql, "security"),
                "performance": executor.submit(self.validate, sql, "performance"),
                "execution": executor.submit(self._execute_query_impl, sql, 100)
            }
            
            # Collect results
            results = {name: future.result() for name, future in futures.items()}
            
            # Debug logging
            logger.info(f"Validation results: {results}")
            
            # Cache results
            cache_key = self._get_cache_key(f"{sql}:{hash(str(business_context))}")
            self._cache_result(cache_key, results)
            
            return self._format_validation_response(sql, results)
    
    def _format_validation_response(self, sql: str, results: Dict) -> Dict[str, Any]:
        """Format validation response."""
        # Handle both boolean and dictionary validation results
        def get_validation_result(result, key, default=False):
            if isinstance(result, bool):
                return result
            elif isinstance(result, dict):
                return result.get(key, default)
            else:
                return default
        
        validation = {
            "syntax_valid": get_validation_result(results["syntax"], "valid", False),
            "business_compliant": get_validation_result(results["business"], "valid", False),
            "security_valid": get_validation_result(results["security"], "valid", False),
            "performance_issues": results["performance"].get("issues", []) if isinstance(results["performance"], dict) else []
        }
        
        # Debug logging
        logger.info(f"Formatted validation: {validation}")
        
        final_result = {
            "success": True,
            "generated_sql": sql,
            "validation": validation,
            "query_execution": results["execution"],
            "is_valid": all([
                validation["syntax_valid"],
                validation["business_compliant"],
                validation["security_valid"]
            ])
        }
        
        logger.info(f"Final SQL generation result: {final_result}")
        return final_result
    
    def _format_response_with_cache(self, sql: str, cached_results: Dict) -> Dict[str, Any]:
        """Format response using cached validation results."""
        return {
            "success": True,
            "generated_sql": sql,
            "validation": cached_results,
            "cached": True,
            "is_valid": cached_results.get("syntax_valid", False)
        }
    
    def _build_query_prompt(self, user_query: str, business_context: Dict, entity_context: Dict) -> str:
        """Build query prompt."""
        business_instructions = business_context.get("business_instructions", [])
        
        # Get top 2 entities and fetch their schemas efficiently
        entities = entity_context.get("entities", [])
        schema_info = "No schema information available"
        
        if entities:
            schema_parts = []
            # depth = self._get_schema_depth(user_query) ----->the scaling of tables
            # print(f"DEBUG schema depth: {depth} for query: {user_query}", flush=True)
            # for top_entity in entities[:depth]:
            for top_entity in entities[:2]:  # top 2 entities
                try:
                    schema_result = self.database_tools.get_table_schema_unified(top_entity)
                    columns = [col['name'] for col in schema_result.get('columns', [])]
                    schema_parts.append(f"{top_entity} columns: {', '.join(columns)}")
                except Exception as e:
                    logger.error(f"Failed to fetch schema for {top_entity}: {e}")
            schema_info = "\n".join(schema_parts) if schema_parts else "No schema information available"
        
        business_context_str = ""
        if business_instructions:
            business_context_str = "Business context:\n"
            for instruction in business_instructions[:3]:
                business_context_str += f"- {instruction.get('instructions', '')}\n"
        
        return f"""
            Generate Oracle SQL for the following request: {user_query}
            
            Most relevant table schemas:
            {schema_info}
            
            {business_context_str}
            
            Instructions:
            0. For simple queries write SQL directly using the schema above
            1. Generate the Oracle SQL query and call final_answer() with it as a string
            2. The database is Oracle - use Oracle syntax only
            3. ALWAYS use final_answer("your sql here") - never write raw SQL outside final_answer()
            4. Never use ```sql code blocks - write plain Python only
  


            IMPORTANT Oracle SQL rules:
            - Use FETCH FIRST N ROWS ONLY instead of TOP N, when asked.
            - Use SYSDATE instead of NOW() or GETDATE(), when asked.
            - Don't use ISNULL(), unless asked.
            - SYSDATE has no parentheses, never write SYSDATE()
            - Never add WHERE conditions not explicitly asked for by the user
            """


    def _build_query_prompt2(self, user_query: str, business_context: Dict, entity_context: Dict) -> str:
        print(f"DEBUG entity_context keys: {entity_context.keys()}", flush=True)
        print(f"DEBUG entity_context: {entity_context}", flush=True)
        """Build query prompt."""
        schema_info = self._format_schema_info(entity_context.get("table_schemas", {}))
        business_instructions = business_context.get("business_instructions", [])
        
        business_context_str = ""
        if business_instructions:
            business_context_str = "Business context:\n"
            for instruction in business_instructions[:3]:  # Limit to top 3
                business_context_str += f"- {instruction.get('instructions', '')}\n"
        
        return f"""
        Generate Oracle SQL for the following request: {user_query}
        
        Available schema information:
        {schema_info}
        
        {business_context_str}
        
        Instructions:
        1. For simple queries, write the SQL directly without checking tables first
        2. The database is Oracle - use Oracle syntax only
        3. To get table list if needed: tables = get_all_tables_unified_tool()['tables']
        4. Test using execute_query_and_return_results(query_string)
        5. Call final_answer(sql_query_string) with ONLY the SQL string

        Examples:
        - final_answer("SELECT COUNT(*) FROM address")
        - final_answer("SELECT table_name FROM all_tables")
        - final_answer("SELECT * FROM address FETCH FIRST 10 ROWS ONLY")

        IMPORTANT Oracle SQL rules:
        - Use ALL_TABLES or USER_TABLES instead of INFORMATION_SCHEMA
        - Use FETCH FIRST N ROWS ONLY instead of TOP N
        - Use SYSDATE instead of NOW() or GETDATE()
        - Use TRUNC(date) for date-only comparisons
        - Never use square brackets for column names
        - Use NVL() instead of ISNULL()
        - For COUNT queries, just write SELECT COUNT(*) FROM tablename directly
        """
    
    def _format_schema_info(self, table_schemas: Dict) -> str:
        """Format schema information for prompt."""
        if not table_schemas:
            return "No schema information available"
        
        schema_lines = []
        for table_name, schema in table_schemas.items():
            columns = schema.get("columns", [])
            column_names = [col.get("name", "") for col in columns if col.get("name")]
            if column_names:
                schema_lines.append(f"{table_name}: {', '.join(column_names)}")
        
        return "\n".join(schema_lines) if schema_lines else "No valid schema information"
    
    def _extract_sql_from_response(self, response) -> Optional[str]:
        """Extract SQL from agent response."""
        if hasattr(response, 'text'):
            response = response.text
        
        # Handle dictionary response (from final_answer tool)
        if isinstance(response, dict):
            if 'final_sql' in response:
                return response['final_sql']
            elif 'sql' in response:
                return response['sql']
            elif 'query' in response:
                return response['query']
            elif 'error' in response:
                logger.error(f"Agent returned error: {response['error']}")
                return None
        
        if isinstance(response, str):
            import re
            sql_pattern = r'```sql\s*(.*?)\s*```'
            match = re.search(sql_pattern, response, re.DOTALL)
            if match:
                return match.group(1).strip()
            
            final_answer_pattern = r'final_answer\s*\(\s*["\']([^"\']*)["\']'
            match = re.search(final_answer_pattern, response)
            if match:
                return match.group(1).strip()
            
            get_accurate_schema_pattern = r'get_accurate_schema\s*\(\s*["\']([^"\']*)["\']'
            match = re.search(get_accurate_schema_pattern, response)
            if match:
                return match.group(1).strip()
            
            lines = response.split('\n')
            sql_lines = []
            for line in lines:
                if any(keyword in line.upper() for keyword in ['SELECT', 'FROM', 'WHERE', 'JOIN', 'GROUP', 'ORDER']):
                    sql_lines.append(line.strip())
            
            if sql_lines:
                return '\n'.join(sql_lines)
        
        logger.warning(f"Could not extract SQL from response: {type(response)} - {response}")
        return None

    def _check_business_compliance(self, query: str, business_context: Dict) -> Dict:
        matched_concepts = business_context.get("matched_concepts", [])
        # If no concepts defined, always pass compliance
        if not matched_concepts:
            return {"valid": True, "message": "No concepts defined, compliance check skipped"}
        try:
            return self.business_validator.validate_against_concepts(query, matched_concepts)
        except Exception as e:
            logger.error(f"Business compliance check failed: {e}")
            return {"valid": True, "error": str(e)}

    def _check_business_compliance2(self, query: str, business_context: Dict) -> Dict:
        """Check business compliance of query."""
        matched_concepts = business_context.get("matched_concepts", [])
        try:
            return self.business_validator.validate_against_concepts(query, matched_concepts)
        except Exception as e:
            logger.error(f"Business compliance check failed: {e}")
            return {"success": False, "error": str(e)}
    
    def _execute_query_impl(self, query: str, max_rows: int = 100) -> Dict:
        """Implementation of query execution."""
        try:
            result = self.database_tools.execute_query_safe(query, max_rows)
            
            if not result.get("success"):
                return result
            
            rows = result.get("rows", [])
            columns = result.get("columns", [])
            
            return {
                "success": True,
                "total_rows": len(rows),
                "returned_rows": len(rows),
                "truncated": len(rows) >= max_rows,
                "sample_data": self._create_sample_summary(rows, columns)
            }
            
        except Exception as e:
            logger.error(f"Query execution failed: {e}")
            return {"success": False, "error": str(e)}
    
    def _create_sample_summary(self, rows: List[Dict], columns: List[str]) -> Dict[str, Any]:
        """Create summary of sample data."""
        if not rows:
            return {"message": "No data returned"}
        
        sample_rows = rows[:5]  # First 5 rows
        
        # Calculate numeric statistics
        numeric_stats = {}
        for col in columns:
            numeric_values = [
                row.get(col) for row in rows 
                if row.get(col) is not None and isinstance(row.get(col), (int, float))
            ]
            if numeric_values:
                numeric_stats[col] = {
                    "min": min(numeric_values),
                    "max": max(numeric_values),
                    "avg": round(sum(numeric_values) / len(numeric_values), 2)
                }
        
        return {
            "sample_rows": sample_rows,
            "columns": columns,
            "numeric_stats": numeric_stats
        }
    
    # Legacy method for compatibility
    def generate_sql(self, user_query: str, business_context: Dict, entity_context: Dict) -> Dict[str, Any]:
        """Legacy SQL generation method."""
        return self.generate_sql_optimized(user_query, business_context, entity_context)
    
    def _format_final_sql_response(self, sql_query: str) -> Dict:
        """Return the final SQL answer.
        
        Args:
            sql_query: The final SQL query to return.
            
        Returns:
            Dictionary with the final SQL query and success status.
        """
        try:
            return {
                "success": True,
                "final_sql": sql_query.strip(),
                "message": "Final SQL query generated"
            }
        except Exception as e:
            return {"success": False, "error": str(e)}
        



            #     return f"""
            # Generate Oracle SQL for the following request: {user_query}
            
            # Most relevant table schemas:
            # {schema_info}
            
            # {business_context_str}
            
            # Instructions:
            # 1. For simple queries write SQL directly using the schema above
            # 2. The database is Oracle - use Oracle syntax only
            # 3. Call final_answer(sql_query_string) with ONLY the SQL string
            # 4. Always wrap code in python code blocks, never sql code blocks
            
            # Examples:
            #         Correct format:
            #         final_answer("SELECT COUNT(*) FROM address WHERE status = 'Actual'")
        
            #         Wrong format:
            #         ```sql
            #                 final_answer(...)
            #         ```