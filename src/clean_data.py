import pandas as pd

df = pd.read_csv("data/raw/export.csv")

therms = df["therms"].str.replace(",","")

df["therms"] = pd.to_numeric(therms ,errors ="coerce")
#first 5 rows of therms
print(df["therms"].head())

print("Data Type:", df["therms"].dtype)
print("----------------------------")

cost = df["cost"].str.replace(",","")


df["cost"] = pd.to_numeric(cost, errors = "coerce")
#first 5 rows of cost
print(df["cost"].head())


print(df["cost"].dtype)
print("----------------------------")

df["start_date"] = pd.to_datetime(df["start_date"], format= "%Y %b %d %I:%M:%S %p" , errors = "coerce")

print("\nStart Day:")
print(df["start_date"].head())

print("\nData type:")
print(df["start_date"].dtype)
print("----------------------------")

df["end_date"] = pd.to_datetime(df["end_date"], format = "%Y %b %d %I:%M:%S %p", errors = "coerce")

print("\nEnd Day:")
print(df["end_date"].head())

print("\nData type:")
print(df["end_date"].dtype)
print("----------------------------")

print("\nInvalid values:")
print(df[["start_date", "end_date", "therms", "cost"]].isna().sum())

#Check negative costs
negative_cost = df[df["cost"] < 0]
print("\nNegative costs:")
print(len(negative_cost))

#Check for invalid date rages
invalid_dates = df[df["start_date"] >= df["end_date"]]
print("\nInvalid date ranges:")
print(len(invalid_dates))

#Check duplicate 
duplicate = df.duplicated(subset=["start_date","end_date"])
print("\nDuplicate billing periods:")
print(duplicate.sum())

#check negative therms
negative_therms = df[df["therms"] < 0]

print("\nNegative therms:")
print(len(negative_therms))