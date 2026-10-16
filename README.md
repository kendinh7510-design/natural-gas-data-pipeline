# Natural Gas Data Analytics & ETL Pipeline

## Overview

I built this project to practice data engineering using Python, Pandas, SQL, and PostgreSQL.

The project uses historical natural gas consumption data from the [CBU Service Center Natural Gas dataset](https://catalog.data.gov/dataset/cbu-service-center-natural-gas). It contains 197 records with billing dates, gas consumption (therms), and costs.

The goal is to clean and validate the data, load it into PostgreSQL, and use SQL to analyze consumption and cost patterns.

## Technologies

- **Python & Pandas** — Data cleaning and transformation
- **PostgreSQL** — Data storage and SQL analysis
- **Psycopg** — Python and PostgreSQL connection
- **pytest** — Unit testing
- **Python Logging** — Pipeline monitoring and error tracking

## ETL Pipeline

The pipeline consists of four main steps:

1. **Extract:** Read the raw data from a CSV file.
2. **Transform:** Convert dates and numeric columns into the correct data types.
3. **Validate:** Check for missing values, negative consumption or costs, invalid date ranges, and duplicate billing periods.
4. **Load:** Insert validated records into PostgreSQL.

I used database constraints to prevent invalid records and `ON CONFLICT DO NOTHING` to skip duplicate billing periods when the pipeline runs multiple times.

The pipeline also uses transactions to avoid partially committed data if an insert fails.

## SQL Analysis

After loading the data into PostgreSQL, I wrote SQL queries to analyze:

- Total and average gas consumption and costs
- Yearly gas consumption and cost trends
- Average cost per therm
- Low, medium, and high cost categories
- Consumption patterns using `GROUP BY`, `HAVING`, and CTEs

I also created a SQL View to reuse the yearly consumption summary without rewriting the same query.

Yearly summaries group records by their billing period's start year.

## Results

| Metric | Result |
|---|---:|
| Total records | 197 |
| Total consumption | 233,213.811 therms |
| Total cost | $129,566.18 |
| Average consumption per period | 1,183.826 therms |
| Overall cost per therm | $0.5556 |

## Testing and Logging

I used pytest to test five scenarios:

- Valid data
- Invalid date ranges
- Negative gas consumption
- Negative costs
- Duplicate billing periods

All five tests passed.

I also added logging to track pipeline execution, processed records, and errors. Logs are written to both the terminal and a local log file.

## Running the Project

Install the dependencies:

```bash
pip install -r requirements.txt
```

Create a PostgreSQL database named `natural_gas_db`, configure `.env` using `.env.example`, and run `sql/create_tables.sql`.

Run the ETL pipeline:

```bash
python src/pipeline.py
```

Run the tests:

```bash
python -m pytest tests/ -v
```

The SQL analysis scripts are available in the `sql/` directory.
