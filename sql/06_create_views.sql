
-- Reusable yearly consumption summary view
CREATE OR REPLACE VIEW yearly_gas_summary AS
SELECT
    EXTRACT(YEAR FROM start_date) AS usage_year,
    SUM(therms) AS total_therms,
    SUM(cost) AS total_cost,
    COUNT(*) AS total_periods
FROM gas_usage
GROUP BY EXTRACT(YEAR FROM start_date);

-- Query the view

SELECT *
FROM yearly_gas_summary
ORDER BY total_therms DESC;
