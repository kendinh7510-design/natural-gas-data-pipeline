import pandas as pd
from db_connection import get_connection

df = pd.read_csv("data/raw/export.csv")

#convert numeric columns
therms = df["therms"].str.replace(",","")
df["therms"] = pd.to_numeric( therms, errors = "coerce")

cost = df["cost"].str.replace(",","")
df["cost"] = pd.to_numeric(cost, errors = "coerce")

# Convert date columns
date_format = "%Y %b %d %I:%M:%S %p"

df["start_date"] = pd.to_datetime(df["start_date"], format = date_format, errors = "coerce")

df["end_date"] = pd.to_datetime(df["end_date"],format= date_format, errors = "coerce")



with get_connection() as conn:
    with conn.cursor() as cursor:
        for index,row in df.iterrows():
            cursor.execute("""
                INSERT INTO gas_usage (therms,cost,start_date,end_date) VALUES(%s,%s,%s,%s) ON CONFLICT (start_date, end_date) DO NOTHING;

            """,(float(row["therms"]),
                float(row["cost"]),
                row["start_date"].date(),
                row["end_date"].date()
                )  
            
            )
            inserted_rows += cursor.rowcount
            print("Rows inserted:" ,cursor.rowcount, "total is:" ,inserted_rows)