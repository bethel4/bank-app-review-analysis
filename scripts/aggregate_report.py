import pandas as pd


def main():
    df = pd.read_csv("data/reviews_with_sentiment_and_themes.csv")

    agg_sentiment = (
        df.groupby(["bank_name", "rating"])["sentiment_score"].mean().reset_index()
    )
    print("Average sentiment score by bank and rating:")
    print(agg_sentiment)

    theme_counts = (
        df.groupby(["bank_name", "identified_themes"]).size().reset_index(name="count")
    )
    print("\nReview counts by theme and bank:")
    print(theme_counts)

    agg_sentiment.to_csv("data/agg_sentiment_by_bank_rating.csv", index=False)
    theme_counts.to_csv("data/theme_counts_by_bank.csv", index=False)
    print("Saved aggregated reports.")


if __name__ == "__main__":
    main()
