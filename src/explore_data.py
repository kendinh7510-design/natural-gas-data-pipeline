import pandas as pd

#read file
df = pd.read_csv("data/raw/export.csv")

#Display first 5 rows
print("First 5 rows")
print(df.head())

#Display dataset information
print("\nDataset information:")
print(df.info())

#Display number of rows and columns
print("\nDataset shape:")
print(df.shape)

#Display missing values per column
print("\nMissing values:")
print(df.isnull().sum())

#Duplicate rows 
print("\nDuplicate rows:")
print(df.duplicated().sum())

#Check data types
print("\nData types:")
print(df.dtypes)
