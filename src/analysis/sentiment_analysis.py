from transformers import pipeline
import pandas as pd


def analyze_sentiment_distilbert(df, text_column="review"):
    classifier = pipeline(
        "sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english"
    )

    results = classifier(df[text_column].tolist(), truncation=True, max_length=512)
    df["sentiment_label"] = [r["label"].lower() for r in results]
    df["sentiment_score"] = [r["score"] for r in results]

    return df
