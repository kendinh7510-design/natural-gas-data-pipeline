import pandas as pd
from db_connection import get_connection
from logger import setup_logger

logger = setup_logger()

#Extract Function
def extract():
    df = pd.read_csv("data/raw/export.csv")
    return df

#Transform Function
def transform(df):
    #copy a dataframe
    df = df.copy()

    therms = df["therms"].str.replace(",","")
    df["therms"] = pd.to_numeric(therms, errors = "coerce")

    cost = df["cost"].str.replace(",","")
    df["cost"] = pd.to_numeric(cost, errors = "coerce")

    format_date = "%Y %b %d %I:%M:%S %p"
    df["start_date"] = pd.to_datetime(df["start_date"], format = format_date, errors = "coerce")

    df["end_date"] = pd.to_datetime(df["end_date"], format= format_date, errors= "coerce")

    return df

#Data Validation
def validate(df):
     # Check missing or invalid values
    missing = df.isna().sum().sum()

     # Check negative consumption
    negative_therms = (df["therms"] < 0).sum()

     # Check negative costs
    negative_cost = (df["cost"] < 0).sum()

     # Check invalid date ranges
    invalid_dates = (df["start_date"] >= df["end_date"]).sum()

     # Check duplicate billing periods
    duplicate = df.duplicated(subset = ["start_date","end_date"]).sum()
     
    print("\nData Validation Results:")
    print("Missing values:", missing)
    print("Negative therms:", negative_therms)
    print("Negative costs:", negative_cost)
    print("Invalid date ranges:", invalid_dates)
    print("Duplicate billing periods:", duplicate)

    total_issues = missing + negative_therms + negative_cost + invalid_dates+ duplicate
    if total_issues > 0:
        raise ValueError("Data validation failed!")
    return df

def load(df):
    inserted = 0

    with get_connection() as conn:
        with conn.cursor() as cursor:
            for index,row in df.iterrows():
                cursor.execute("""
                    INSERT INTO gas_usage (therms,cost,start_date,end_date) VALUES(%s,%s,%s,%s) 
                    ON CONFLICT (start_date,end_date) DO NOTHING """,
                    ( float(row["therms"]),
                    float(row["cost"]),
                    row["start_date"].date(),
                    row["end_date"].date()
                    )
                    )
                inserted += cursor.rowcount
    print("\nRecords inserted:", inserted)
    return inserted

if __name__ == "__main__":
    try:
        logger.info("ETL pipeline started")

        raw_df = extract()
        logger.info("Extracted %d records", len(raw_df))
        
        clean_df = transform(raw_df)
        logger.info("Data transformation completed")
        
        valid_df = validate(clean_df)
        logger.info("Validated %d records", len(valid_df))

        inserted = load(valid_df)
        logger.info("Inserted %d new records", inserted)

        logger.info("ETL pipeline completed successfully")

    except Exception:
        logger.exception("ETL pipeline failed")
        raise

    