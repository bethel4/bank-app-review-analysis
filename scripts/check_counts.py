import pandas as pd

df = pd.read_csv("data/cleaned_reviews.csv")
print(df['bank'].value_counts())
print("Total reviews:", len(df))