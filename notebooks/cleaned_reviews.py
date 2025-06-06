import pandas as pd

# Load cleaned CSV
df = pd.read_csv("data/cleaned_reviews.csv")

# Preview data
display(df.head())

# Check for duplicates
print("Duplicates:", df.duplicated().sum())

# Check for missing values
print("\nMissing values:\n", df.isnull().sum())

# Confirm date format
try:
    pd.to_datetime(df["date"], format="%Y-%m-%d", errors="raise")
    print("\n Dates are correctly formatted.")
except Exception as e:
    print("\n Date format issue:", e)

# Check column order
print("\nColumns:", df.columns.tolist())

# Optional summary
df.info()
