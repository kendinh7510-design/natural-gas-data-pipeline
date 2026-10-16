
-- Cost per therm for each billing period
SELECT
    usage_id,
    start_date,
    end_date,
    therms,
    cost,
    ROUND(cost / NULLIF(therms, 0), 4) AS cost_per_therm
FROM gas_usage
ORDER BY start_date;

-- Compare simple average vs weighted average

SELECT
    ROUND(
        AVG(cost / NULLIF(therms, 0)), 4
    ) AS average_cost_per_therm,

    ROUND(
        SUM(cost) / NULLIF(SUM(therms), 0), 4
    ) AS overall_cost_per_therm
FROM gas_usage;
