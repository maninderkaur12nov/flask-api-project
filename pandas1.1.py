import pandas as pd
from tabulate import tabulate # type: ignore
df=pd.read_csv("train.csv")
# print("\n first 5 rows")
# print(df.head)
# print(tabulate(df.head(), headers='keys', tablefmt='pretty'))
# print(tabulate(df.head(), headers='keys', tablefmt='grid'))
# print(tabulate(df.head(), headers='keys', tablefmt='fancy_grid'))
# # print(tabulate(df.head(), headers='keys', tablefmt='pipe'))
# print("\n shape:",df.shape)
# print("\n name: info")
# print(df.info)
# print("\n  missing values")
# print(df.isnull().sum())

# Fill Age with average

# df["Age"]=df["Age"].fillna(df["Age"].mean())
# df["Embarked"]=df["Embarked"].fillna(df["Embarked"].mode()[0])
# df.drop("Cabin", axis=1, inplace=True)
# print("Missing values (after cleaning):")
# print(df.isnull().sum())
# df.describe()

# Fill missing Age values with the average age
df["Age"] = df["Age"].fillna(df["Age"].mean())

# Fill missing Embarked values with the most frequent port
df["Embarked"] = df["Embarked"].fillna(df["Embarked"].mode()[0])

# Drop the Cabin column due to too many missing values
df.drop("Cabin", axis=1, inplace=True)

# Verify no missing values remain
print("Missing values after cleaning:\n", df.isnull().sum())

# Save cleaned dataset to a new CSV file
df.to_csv("titanic_cleaned.csv", index=False)
print("Cleaned data saved to titanic_cleaned.csv")

