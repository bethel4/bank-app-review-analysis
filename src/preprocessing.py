# src/scraper/preprocessing.py

import pandas as pd
import os


def preprocess_reviews(df: pd.DataFrame) -> pd.DataFrame:
    df = df.drop_duplicates(subset=["review", "date"])
    df = df.dropna(subset=["review", "rating", "date"])
    df["date"] = pd.to_datetime(df["date"]).dt.strftime("%Y-%m-%d")
    return df


def save_reviews_to_csv(
    df: pd.DataFrame, filename: str = "data/cleaned_reviews.csv"
) -> None:
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    df[["review", "rating", "date", "bank", "source"]].to_csv(filename, index=False)
