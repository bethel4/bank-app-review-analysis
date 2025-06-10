import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer


def extract_keywords(corpus, top_n=20):
    vectorizer = TfidfVectorizer(ngram_range=(1, 2), max_features=1000)
    X = vectorizer.fit_transform(corpus)
    tfidf_scores = X.sum(axis=0).A1
    keywords = vectorizer.get_feature_names_out()
    scores = sorted(zip(keywords, tfidf_scores), key=lambda x: x[1], reverse=True)
    return [kw for kw, score in scores[:top_n]]


def assign_themes(text, bank, themes_per_bank):
    matched_themes = []
    for theme, keywords in themes_per_bank.get(bank, {}).items():
        for kw in keywords:
            if kw in text:
                matched_themes.append(theme)
                break
    if not matched_themes:
        matched_themes = ["Other"]
    return "; ".join(matched_themes)


def main():
    df = pd.read_csv("data/reviews_with_sentiment.csv")

    themes_per_bank = {}

    for bank in df["bank_name"].unique():
        bank_texts = df.loc[df["bank_name"] == bank, "clean_text"]
        keywords = extract_keywords(bank_texts)
        print(f"Top keywords for {bank}: {keywords}")

        # Manual theme grouping, edit these keywords as you see fit
        themes_per_bank[bank] = {
            "Account Access Issues": [
                "login error",
                "password reset",
                "account locked",
            ],
            "Transaction Performance": ["slow transfer", "transaction failed", "delay"],
            "User Interface & Experience": ["easy to use", "good ui", "navigation"],
            "Customer Support": ["customer service", "support team", "help desk"],
            "Feature Requests": ["add feature", "new update", "missing option"],
        }

    df["identified_themes"] = df.apply(
        lambda row: assign_themes(row["clean_text"], row["bank_name"], themes_per_bank),
        axis=1,
    )
    df.to_csv("data/reviews_with_sentiment_and_themes.csv", index=False)
    print("Saved file with themes: data/reviews_with_sentiment_and_themes.csv")


if __name__ == "__main__":
    main()
