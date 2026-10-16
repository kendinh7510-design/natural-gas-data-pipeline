SELECT
    COUNT(*) AS total_records,
    SUM(therms) AS total_therms,
    ROUND(AVG(therms), 3) AS average_therms,
    MIN(therms) AS minimum_therms,
    MAX(therms) AS maximum_therms,
    SUM(cost) AS total_cost,
    ROUND(AVG(cost), 2) AS average_cost
FROM gas_usage;