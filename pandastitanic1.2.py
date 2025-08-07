import pandas as pd
from tabulate import tabulate  # type: ignore
df=pd.read_csv("titanic_cleaned.csv")
# 1. Show first 5 rows
print("First 5 rows:")
print(tabulate(df.head(),headers='keys',tablefmt='grid'))


# 2. Summary statistics of numeric columns
print("\nSummary statistics:")
print(df.describe())

# 3. Count of missing values per column
print("\nMissing values count:")
print(df.isnull().sum())

# 4. Survival rate overall
print("\nOverall survival rate:")
print(df['Survived'].value_counts(normalize=True))


# 5. Survival rate by gender
print("\nSurvival rate by Sex:")
print(df.groupby('Sex')['Survived'].mean())

# 6. Survival rate by passenger class
print("\nSurvival rate by Pclass:")
print(df.groupby('Pclass')['Survived'].mean())

# Check again for any missing values
print("\nMissing values after cleaning:")
print(df.isnull().sum())
