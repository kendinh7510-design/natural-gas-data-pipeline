
-- Annual Gas Consumption and Cost Analysis

SELECT
    EXTRACT(YEAR FROM start_date) AS usage_year,
    SUM(therms) AS total_therms,
    SUM(cost) AS total_cost,
    COUNT(*) AS total_periods
FROM gas_usage
GROUP BY EXTRACT(YEAR FROM start_date)
ORDER BY usage_year;

-- Find the year with the highest consumption

SELECT
    EXTRACT(YEAR FROM start_date) AS usage_year,
    SUM(therms) AS total_therms
FROM gas_usage
GROUP BY EXTRACT(YEAR FROM start_date)
ORDER BY total_therms DESC
LIMIT 1;
