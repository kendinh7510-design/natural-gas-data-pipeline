
-- Classify billing periods by cost
-- Thresholds are illustrative, not official utility categories
WITH cost_categories AS (
    SELECT
        usage_id,
        cost,
        CASE
            WHEN cost < 300 THEN 'Low Cost'
            WHEN cost < 1000 THEN 'Medium Cost'
            ELSE 'High Cost'
        END AS cost_category
    FROM gas_usage
)
SELECT
    cost_category,
    COUNT(*) AS total_periods,
    SUM(cost) AS total_cost
FROM cost_categories
GROUP BY cost_category
ORDER BY total_periods DESC;
