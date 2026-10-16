# Natural Gas Data Analytics & ETL Pipeline

## Project Overview

This project demonstrates the development of an end-to-end ETL (Extract, Transform, Load) pipeline using Python, Pandas, and PostgreSQL.

The pipeline processes historical natural gas consumption and cost data, performs data cleaning and validation, and loads the results into a relational database for SQL-based analysis.

The project focuses on data quality, database integrity, reusable SQL queries, automated testing, and error logging.

## Dataset

**Source:** [CBU Service Center Natural Gas — Data.gov](https://catalog.data.gov/dataset/cbu-service-center-natural-gas)

The dataset contains 197 records of natural gas consumption and costs.

| Column | Description |
|---|---|
| `start_date` | Start date of the usage period |
| `end_date` | End date of the usage period |
| `therms` | Natural gas consumption in therms |
| `cost` | Cost of natural gas consumption |

The data covers billing periods from December 2009 through May 2026.

## Tech Stack

- **Python:** ETL development and automation
- **Pandas:** Data exploration, cleaning, and validation
- **PostgreSQL:** Relational database and SQL analytics
- **Psycopg 3:** Python-to-PostgreSQL connectivity
- **pytest:** Automated unit testing
- **Python Logging:** Pipeline monitoring and error tracking
- **Git:** Version control

## ETL Pipeline Architecture

The ETL workflow consists of four main stages:

**1. Extract**

Read the source CSV file into a Pandas DataFrame.

**2. Transform**

- Convert consumption and cost values into numeric data types.
- Convert date strings into datetime values.
- Prepare cleaned data for database insertion.

**3. Validate**

Check for:

- Missing or invalid values
- Negative gas consumption
- Negative costs
- Invalid date ranges
- Duplicate billing periods

The current validation strategy raises a `ValueError` and stops the pipeline if any record fails validation.

**4. Load**

Load validated records into PostgreSQL using Psycopg.

The pipeline uses parameterized SQL statements and `ON CONFLICT DO NOTHING` to prevent duplicate billing periods from being inserted during repeated runs.

Database transactions help ensure that a failed load does not leave partially committed data.

## Database Design

The PostgreSQL database contains a `gas_usage` table with the following columns:

| Column | Data Type |
|---|---|
| `usage_id` | SERIAL PRIMARY KEY |
| `start_date` | DATE |
| `end_date` | DATE |
| `therms` | NUMERIC(12,3) |
| `cost` | NUMERIC(12,2) |
| `created_at` | TIMESTAMP |

Database constraints enforce nonnegative consumption and cost values, valid date ranges, and unique billing periods.

**Design assumption:** The source data represents a single facility. Therefore, the combination of `start_date` and `end_date` is used as the unique billing-period key. A multi-customer system would require a more specific identifier, such as a customer, account, or meter ID.

## SQL Analytics

Reusable SQL scripts provide:

- Overall consumption and cost statistics
- Annual consumption and cost summaries
- Cost-per-therm calculations
- Cost category classification using `CASE WHEN`
- Aggregations using `GROUP BY`
- Filtering aggregated results using `HAVING`
- Common Table Expressions (CTEs)
- Reusable reporting views

The `yearly_gas_summary` view provides annual consumption, cost, and record counts.

**Reporting assumption:** Billing periods are assigned to the year of their `start_date`. Consumption crossing calendar-year boundaries is not split between years.

## Key Findings

The following results were obtained from the 197 loaded records:

| Metric | Result |
|---|---:|
| Total records | 197 |
| Total gas consumption | 233,213.811 therms |
| Total cost | $129,566.18 |
| Average consumption per billing period | 1,183.826 therms |
| Overall cost per therm | $0.5556 |
| Highest consumption year by start date | 2011 |

The cost-per-therm metric is calculated by dividing total cost by total consumption.

## Automated Testing

The project uses `pytest` to test data validation behavior.

Five unit tests have been implemented:

1. Valid data acceptance
2. Invalid date range detection
3. Negative consumption detection
4. Negative cost detection
5. Duplicate billing period detection

All five tests passed during local testing.

Tests use sample DataFrames and do not modify the production dataset or PostgreSQL records.

## Logging and Error Handling

Python's built-in logging module records pipeline execution events.

The logs include:

- Pipeline start and completion
- Number of records extracted and validated
- Number of records inserted
- Error messages and tracebacks

Log messages are written to the terminal and `logs/etl.log`.

Exceptions are logged and re-raised to ensure failures are visible.

Create a `.env` file in the project root and configure:

```dotenv
DB_HOST=localhost
DB_PORT=5432
DB_NAME=natural_gas_db
DB_USER=postgres
DB_PASSWORD=your_password
```
Replace the example credentials with your own local configuration. 

## Future Improvements

Potential improvements include:

- Separating invalid records into a rejection dataset
- Adding integration tests for database operations
- Implementing scheduled pipeline execution
- Adding data visualization dashboards
- Supporting multiple facilities and utility meters

## Project Purpose

This project was developed as a practical learning exercise to strengthen skills in Python, SQL, ETL development, data quality management, and relational databases.
