# Oracle SQL lessons for this database

## Table selection
- Main address table is `address` — use it by default for address-related questions
- cleanup_* tables are derived/processing tables, only use if explicitly asked
- When asked about "addresses" without qualification, always query `address` table
- address_relation links addresses together, join on entity_identity to source_identity

## Oracle syntax
- Empty string '' equals NULL in Oracle, never use != '', use IS NOT NULL
- Use SYSDATE not NOW() or GETDATE(), and never SYSDATE()
- Use FETCH FIRST N ROWS ONLY not TOP N
- Use NVL() not ISNULL()
- COUNT in UNION ALL must be aliased: SELECT COUNT(*) as cnt
- UNION ALL with FETCH FIRST must wrap in subquery: SELECT SUM(cnt) FROM (...)
- Use COUNT(*) for simple row counts, only use COUNT(DISTINCT entity_identity) when "unique" or "distinct" is explicitly mentioned

## Column names
- Source system is stored in column `source_name` not `source`
- Status values are case-sensitive: 'Obsolete', 'Actual'
- Date created is `create_timestamp`, date updated is `update_timestamp`
- City is stored in `city_name`, street in `street_name`, postal code in `postal_code`

## Query patterns
- For percentage: ROUND(COUNT(CASE WHEN x THEN 1 END) * 100 / COUNT(*), 2)
- For missing values: column IS NULL (not = '' or != '')
- Never add WHERE conditions not explicitly asked for by the user
-- Use COUNT(*) for simple row counts, only use COUNT(DISTINCT entity_identity) when "unique" or "distinct" is explicitly mentioned in the question