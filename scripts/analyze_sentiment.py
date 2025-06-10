import sys
import os

sys.path.insert(
    0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src"))
)

import pandas as pd
from analysis.sentiment_analysis import analyze_sentiment_distilbert
from analysis.thematic_analysis import (
    extract_themes,
)  # Assuming you've already built this

# Load preprocessed reviews
df = pd.read_csv("data/cleaned_reviews.csv")

# Run sentiment analysis using DistilBERT
df = analyze_sentiment_distilbert(df)

# Run theme extraction (TF-IDF-based)
df = extract_themes(df)

# Save the annotated dataset
df.to_csv("data/sentiment_themes.csv", index=False)
print(" Sentiment and themes saved to data/sentiment_themes.csv")
