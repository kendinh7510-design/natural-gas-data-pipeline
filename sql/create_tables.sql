
CREATE TABLE IF NOT EXISTS gas_usage (
    usage_id SERIAL PRIMARY KEY,
    therms NUMERIC(12,3) NOT NULL,
    cost NUMERIC(12,2) NOT NULL,
    start_date DATE NOT NULL,
    end_date DATE NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT valid_dates
        CHECK (start_date < end_date),

    CONSTRAINT valid_therms
        CHECK (therms >= 0),

    CONSTRAINT valid_cost
        CHECK (cost >= 0),

    CONSTRAINT unique_billing_period
        UNIQUE (start_date, end_date)
);
