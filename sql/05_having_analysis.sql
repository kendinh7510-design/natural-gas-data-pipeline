-- Find years with high consumption and high costs
SELECT
    EXTRACT(YEAR FROM start_date) AS usage_year,
    SUM(therms) AS total_therms,
    SUM(cost) AS total_cost
FROM gas_usage
GROUP BY EXTRACT(YEAR FROM start_date)
HAVING SUM(therms) > 15000
   AND SUM(cost) > 8000
ORDER BY usage_year DESC;
