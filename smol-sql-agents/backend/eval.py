"""
SmolSQLAgents Evaluation Pipeline
Run sequentially: python eval.py
"""

import requests
import time
import json

BASE_URL = "http://localhost:5000"

# ─────────────────────────────────────────────
# TEST CASES
# Add more cases following the same structure
# ─────────────────────────────────────────────
test_cases = [
    {
        "id": 1,
        "query": "how many addresses have 'Actual' status",
        "type": "sql",
        "expected_tables": ["address"],          # tables entity recognition should find
        "expected_keywords": ["COUNT", "address", "status", "Actual"],  # must appear in SQL
        "expected_result": 10690124,              # expected numeric result (None to skip)
        "expected_result_tolerance": 0,           # allow ± this much difference
    },
    # ── Add more cases here ──
    # {
    #     "id": 2,
    #     "query": "give me a count of addresses by validity value",
    #     "type": "sql",
    #     "expected_tables": ["address"],
    #     "expected_keywords": ["validity", "GROUP BY", "COUNT"],
    #     "expected_result": None,
    # },
    # {
    #     "id": 13,
    #     "query": "which tables are related to the BAG update process",
    #     "type": "discovery",
    #     "expected_tables": ["bag_update_0100", "bag_update_0200"],  # should appear in answer
    #     "expected_keywords": ["bag_update"],
    #     "expected_result": None,
    # },
]

# ─────────────────────────────────────────────
# SCORING LOGIC
# ─────────────────────────────────────────────

def check_keywords(text: str, keywords: list) -> tuple:
    """Check how many keywords appear in text (case insensitive)."""
    text_lower = text.lower()
    found = [k for k in keywords if k.lower() in text_lower]
    missing = [k for k in keywords if k.lower() not in text_lower]
    return found, missing

def check_tables(entity_results: list, expected_tables: list) -> tuple:
    """Check if expected tables were recognized."""
    found = [t for t in expected_tables if t in entity_results]
    missing = [t for t in expected_tables if t not in entity_results]
    return found, missing

def check_result(actual_result, expected_result, tolerance: int = 0) -> bool:
    """Check if numeric result matches expected."""
    if expected_result is None:
        return True  # skip check
    if actual_result is None:
        return False
    return abs(actual_result - expected_result) <= tolerance

def extract_first_number(results: list) -> int:
    """Extract first numeric value from query results."""
    if not results:
        return None
    first_row = results[0]
    for val in first_row.values():
        try:
            return int(val)
        except (ValueError, TypeError):
            continue
    return None

# ─────────────────────────────────────────────
# RUN EVALUATION
# ─────────────────────────────────────────────

def run_eval():
    print("=" * 60)
    print("SmolSQLAgents Evaluation Pipeline")
    print("=" * 60)
    print(f"Running {len(test_cases)} test cases sequentially...\n")

    results = []

    for tc in test_cases:
        print(f"[{tc['id']}] {tc['query']}")
        print("-" * 50)

        start = time.time()
        score = {
            "id": tc["id"],
            "query": tc["query"],
            "type": tc["type"],
            "passed": True,
            "issues": [],
            "sql_generated": "",
            "entities_found": [],
            "result_value": None,
            "elapsed": 0,
        }

        try:
            # Call the query endpoint
            response = requests.post(
                f"{BASE_URL}/api/query",
                json={"query": tc["query"]},
                timeout=120
            )
            elapsed = time.time() - start
            score["elapsed"] = round(elapsed, 2)

            if response.status_code != 200:
                score["passed"] = False
                score["issues"].append(f"HTTP {response.status_code}")
                print(f"  ❌ HTTP error: {response.status_code}")
                results.append(score)
                print()
                continue

            data = response.json()

            if not data.get("success"):
                score["passed"] = False
                score["issues"].append(f"Pipeline failed: {data.get('error', 'unknown')}")
                print(f"  ❌ Pipeline failed: {data.get('error', 'unknown')}")
                results.append(score)
                print()
                continue

            pipeline = data.get("pipeline_results", {})

            # ── Entity recognition check ──
            entities = pipeline.get("entity_recognition", {}).get("entities", [])
            score["entities_found"] = entities
            found_tables, missing_tables = check_tables(entities, tc["expected_tables"])
            if missing_tables:
                score["passed"] = False
                score["issues"].append(f"Missing tables in entity recognition: {missing_tables}")
                print(f"  ⚠️  Entity recognition missed: {missing_tables}")
            else:
                print(f"  ✅ Entity recognition: {found_tables}")

            if tc["type"] == "sql":
                # ── SQL generation check ──
                sql_gen = pipeline.get("sql_generation", {})
                generated_sql = sql_gen.get("generated_sql", "")
                score["sql_generated"] = generated_sql

                if not generated_sql:
                    score["passed"] = False
                    score["issues"].append("No SQL generated")
                    print(f"  ❌ No SQL generated")
                else:
                    print(f"  SQL: {generated_sql[:80]}{'...' if len(generated_sql) > 80 else ''}")

                    # ── Keyword check ──
                    found_kw, missing_kw = check_keywords(generated_sql, tc["expected_keywords"])
                    if missing_kw:
                        score["passed"] = False
                        score["issues"].append(f"Missing keywords: {missing_kw}")
                        print(f"  ⚠️  Missing keywords: {missing_kw}")
                    else:
                        print(f"  ✅ Keywords: all present")

                    # ── Execution check ──
                    exec_result = sql_gen.get("query_execution", {})
                    if not exec_result.get("success"):
                        score["passed"] = False
                        score["issues"].append(f"Query execution failed: {exec_result.get('error', '')}")
                        print(f"  ❌ Execution failed: {exec_result.get('error', '')}")
                    else:
                        print(f"  ✅ Execution succeeded")

                        # ── Result value check ──
                        raw_results = data.get("results", [])
                        result_val = extract_first_number(raw_results)
                        score["result_value"] = result_val

                        if tc.get("expected_result") is not None:
                            tolerance = tc.get("expected_result_tolerance", 0)
                            if check_result(result_val, tc["expected_result"], tolerance):
                                print(f"  ✅ Result: {result_val} (expected {tc['expected_result']})")
                            else:
                                score["passed"] = False
                                score["issues"].append(
                                    f"Wrong result: got {result_val}, expected {tc['expected_result']} ±{tolerance}"
                                )
                                print(f"  ❌ Result: got {result_val}, expected {tc['expected_result']}")

            elif tc["type"] == "discovery":
                # ── Discovery answer check ──
                sql_gen = pipeline.get("sql_generation", {})
                answer = sql_gen.get("answer", "")

                if not answer:
                    score["passed"] = False
                    score["issues"].append("No discovery answer returned")
                    print(f"  ❌ No discovery answer")
                else:
                    print(f"  Answer: {answer[:80]}...")
                    found_kw, missing_kw = check_keywords(answer, tc["expected_keywords"])
                    if missing_kw:
                        score["passed"] = False
                        score["issues"].append(f"Answer missing keywords: {missing_kw}")
                        print(f"  ⚠️  Answer missing: {missing_kw}")
                    else:
                        print(f"  ✅ Answer mentions expected tables/keywords")

        except requests.exceptions.Timeout:
            score["passed"] = False
            score["issues"].append("Request timed out (>120s)")
            score["elapsed"] = 120
            print(f"  ❌ Timeout")

        except Exception as e:
            score["passed"] = False
            score["issues"].append(str(e))
            print(f"  ❌ Error: {e}")

        print(f"  ⏱  {score['elapsed']}s | {'✅ PASS' if score['passed'] else '❌ FAIL'}")
        results.append(score)
        print()

        # Sequential — wait between requests to avoid overloading backend
        time.sleep(1)

    # ─────────────────────────────────────────────
    # FINAL REPORT
    # ─────────────────────────────────────────────
    print("=" * 60)
    print("RESULTS SUMMARY")
    print("=" * 60)

    passed = [r for r in results if r["passed"]]
    failed = [r for r in results if not r["passed"]]
    avg_time = sum(r["elapsed"] for r in results) / len(results) if results else 0

    print(f"Score: {len(passed)}/{len(results)} ({round(len(passed)/len(results)*100)}%)")
    print(f"Avg response time: {round(avg_time, 2)}s")

    if failed:
        print(f"\nFailed cases:")
        for r in failed:
            print(f"  [{r['id']}] {r['query'][:50]}")
            for issue in r["issues"]:
                print(f"       → {issue}")

    print("\nFull results:")
    for r in results:
        status = "✅" if r["passed"] else "❌"
        sql_preview = r["sql_generated"][:50] if r["sql_generated"] else "N/A"
        print(f"  {status} [{r['id']}] {r['elapsed']}s | SQL: {sql_preview}")

    # Save results to JSON for comparison across runs
    with open("eval_results.json", "w") as f:
        json.dump({
            "score": f"{len(passed)}/{len(results)}",
            "pct": round(len(passed)/len(results)*100),
            "avg_time": round(avg_time, 2),
            "results": results
        }, f, indent=2)
    print("\nResults saved to eval_results.json")

if __name__ == "__main__":
    run_eval()