import logging
from typing import Dict, Any, Optional
from pathlib import Path

# Import all agents
from .core import PersistentDocumentationAgent
from .indexer import SQLIndexerAgent
from .entity_recognition import EntityRecognitionAgent
from .business import BusinessContextAgent
from .nl2sql import NL2SQLAgent
from .batch_manager import BatchIndexingManager
from .integration import SQLAgentPipeline

# Import base classes
from .base import BaseAgent, CachingMixin, ValidationMixin

# Import unified database tools
from .tools.factory import DatabaseToolsFactory
from ..database.inspector import DatabaseInspector

logger = logging.getLogger(__name__)

class AgentFactory:
    """Factory for creating and managing agent instances."""
    
    def __init__(self):
        self._instances = {}
        self._shared_llm_model = None
        self._shared_components = {}
        self._unified_database_tools = None
    
    def get_shared_llm_model(self):
        """Get or create shared LLM model."""
        if not self._shared_llm_model:
            from smolagents.models import OpenAIModel
            import os
            
            api_key = os.getenv("OPENAI_API_KEY")
            if not api_key:
                raise ValueError("OPENAI_API_KEY environment variable is not set")
            
            base_url = os.getenv("OPENAI_API_BASE")
            model_id = os.getenv("GROQ_MODEL", "gpt-4o-mini")
            
            self._shared_llm_model = OpenAIModel(
                model_id=model_id,
                api_key=api_key,
                api_base=base_url
            )
            logger.info(f"Shared LLM model created: {model_id} via {base_url}")
        
        return self._shared_llm_model
    
    def get_unified_database_tools(self):
        """Get or create unified database tools."""
        if not self._unified_database_tools:
            database_inspector = DatabaseInspector()
            self._unified_database_tools = DatabaseToolsFactory.create_database_tools(database_inspector)
            logger.info("Unified database tools created")
        
        return self._unified_database_tools
    
    def get_main_agent(self) -> PersistentDocumentationAgent:
        """Get or create main documentation agent."""
        if "main_agent" not in self._instances:
            self._instances["main_agent"] = PersistentDocumentationAgent(
            shared_llm_model=self.get_shared_llm_model()
        )
            logger.info("Main agent created")
        
        return self._instances["main_agent"]
    
    def get_indexer_agent(self) -> SQLIndexerAgent:
        """Get or create indexer agent."""
        if "indexer_agent" not in self._instances:
            from ..vector.store import SQLVectorStore
            
            vector_store = SQLVectorStore()
            self._instances["indexer_agent"] = SQLIndexerAgent(
                vector_store, 
                shared_llm_model=self.get_shared_llm_model()
            )
            logger.info("Indexer agent created")
        
        return self._instances["indexer_agent"]
    
    def get_entity_agent(self) -> EntityRecognitionAgent:
        """Get or create entity recognition agent."""
        if "entity_agent" not in self._instances:
            self._instances["entity_agent"] = EntityRecognitionAgent(
                self.get_indexer_agent(),
                shared_llm_model=self.get_shared_llm_model(),
                database_tools=self.get_unified_database_tools()
            )
            logger.info("Entity recognition agent created")
        
        return self._instances["entity_agent"]
    
    def get_business_agent(self, concepts_dir: str = "src/agents/concepts") -> BusinessContextAgent:
        """Get or create business context agent."""
        if "business_agent" not in self._instances:
            # Get shared components
            shared_concept_loader = self._get_shared_component("concept_loader", concepts_dir)
            shared_concept_matcher = self._get_shared_component("concept_matcher", self.get_indexer_agent())
            
            self._instances["business_agent"] = BusinessContextAgent(
                indexer_agent=self.get_indexer_agent(),
                concepts_dir=concepts_dir,
                shared_llm_model=self.get_shared_llm_model(),
                shared_concept_loader=shared_concept_loader,
                shared_concept_matcher=shared_concept_matcher,
                database_tools=self.get_unified_database_tools()
            )
            logger.info("Business context agent created")
        
        return self._instances["business_agent"]
    
    def get_nl2sql_agent(self, database_tools=None) -> NL2SQLAgent:
        """Get or create NL2SQL agent."""
        if "nl2sql_agent" not in self._instances:
            # Use unified database tools if no specific tools provided
            if database_tools is None:
                database_tools = self.get_unified_database_tools()
            
            self._instances["nl2sql_agent"] = NL2SQLAgent(
                database_tools,
                shared_llm_model=self.get_shared_llm_model()
            )
            logger.info("NL2SQL agent created")
        
        return self._instances["nl2sql_agent"]
    
    def get_batch_manager(self) -> BatchIndexingManager:
        """Get or create batch manager."""
        if "batch_manager" not in self._instances:
            self._instances["batch_manager"] = BatchIndexingManager(
                self.get_indexer_agent()
            )
            logger.info("Batch manager created")
        
        return self._instances["batch_manager"]
    
    def get_sql_pipeline(self, database_tools=None) -> SQLAgentPipeline:
        """Get or create SQL agent pipeline."""
        if "sql_pipeline" not in self._instances:
            # Use unified database tools if no specific tools provided
            if database_tools is None:
                database_tools = self.get_unified_database_tools()
            
            self._instances["sql_pipeline"] = SQLAgentPipeline(
                indexer_agent=self.get_indexer_agent(),
                database_tools=database_tools,
                shared_entity_agent=self.get_entity_agent(),
                shared_business_agent=self.get_business_agent(),
                shared_nl2sql_agent=self.get_nl2sql_agent(database_tools)
            )
            logger.info("SQL agent pipeline created")
        
        return self._instances["sql_pipeline"]
    
    def _get_shared_component(self, component_name: str, *args, **kwargs):
        """Get or create shared component."""
        if component_name not in self._shared_components:
            if component_name == "concept_loader":
                from .concepts.loader import ConceptLoader
                self._shared_components[component_name] = ConceptLoader(*args, **kwargs)
            elif component_name == "concept_matcher":
                from .concepts.matcher import ConceptMatcher
                self._shared_components[component_name] = ConceptMatcher(*args, **kwargs)
            else:
                raise ValueError(f"Unknown shared component: {component_name}")
        
        return self._shared_components[component_name]
    
    def get_all_agents(self) -> Dict[str, Any]:
        """Get all agent instances."""
        return {
            "main_agent": self.get_main_agent(),
            "indexer_agent": self.get_indexer_agent(),
            "entity_agent": self.get_entity_agent(),
            "business_agent": self.get_business_agent(),
            "batch_manager": self.get_batch_manager()
        }
    def initialize(self):
        """Initialize and warm up all agents and indexes."""

        logger.info("Initializing agent ecosystem...")

        # Force creation of core agents
        main_agent = self.get_main_agent()
        self.get_indexer_agent()
        self.get_entity_agent()
        self.get_business_agent()
        self.get_nl2sql_agent()
        self.get_sql_pipeline()

        logger.info("All agents created")

        # Build database knowledge base
        try:
            logger.info("Building database knowledge base...")

            tables = main_agent.db_inspector.get_all_table_names()

            logger.info(f"Found {len(tables)} tables")

            for i, table_name in enumerate(tables):
                try:
                        # Skip if already indexed in ChromaDB - direct ID lookup, no embedding call
                        try:
                            existing = main_agent.indexer_agent.vector_store.table_index.collection.get(ids=[table_name])
                            if existing and existing['ids']:
                                print(f"⏭️ Skipping {table_name} (already indexed)", flush=True)
                                continue
                        except Exception:
                            pass
                            
                        print(f"Processing table {i+1}/{len(tables)}: {table_name}", flush=True)
                        main_agent.process_table_documentation(table_name)
                        print(f"✅ Done: {table_name}", flush=True)
                except Exception as e:
                        print(f"❌ Failed: {table_name}: {e}", flush=True)

            relationships = main_agent.db_inspector.get_all_foreign_key_relationships()

            logger.info(f"Found {len(relationships)} relationships")

            for relationship in relationships:
                try:
                    rel_id = f"{relationship.get('constrained_table')}_{relationship.get('referred_table')}"
                    try:
                        existing = main_agent.indexer_agent.vector_store.relationship_index.collection.get(ids=[rel_id])
                        if existing and existing['ids']:
                            print(f"⏭️ Skipping relationship {rel_id} (already indexed)", flush=True)
                            continue
                    except Exception:
                        pass
                    main_agent.process_relationship_documentation(relationship)
                except Exception as e:
                    logger.error(f"Failed processing relationship: {e}")

            logger.info("Knowledge base build complete")

        except Exception as e:
            logger.error(f"Initialization indexing failed: {e}")

        return self
    def reset(self):
        """Reset all instances (useful for testing)."""
        self._instances.clear()
        self._shared_components.clear()
        self._shared_llm_model = None
        self._unified_database_tools = None
        logger.info("All agent instances reset")

# Global factory instance
agent_factory = AgentFactory() 