# src/scraper/google_play_scraper.py

from google_play_scraper import reviews, Sort
import pandas as pd


def scrape_reviews(app_id: str, bank_name: str, num_reviews: int = 400) -> pd.DataFrame:
    all_reviews = []
    seen_reviews = set()
    next_pagination_token = None

    while len(all_reviews) < num_reviews:
        batch, next_pagination_token = reviews(
            app_id,
            lang="en",
            country="us",
            sort=Sort.NEWEST,
            count=200,
            continuation_token=next_pagination_token,
        )
        if not batch:
            break

        for entry in batch:
            content = entry["content"]
            date = entry["at"]
            if content not in seen_reviews:
                seen_reviews.add(content)
                all_reviews.append(
                    {
                        "review": content,
                        "rating": entry["score"],
                        "date": date,
                        "bank": bank_name,
                        "source": "Google Play",
                    }
                )
            if len(all_reviews) >= num_reviews:
                break

        if next_pagination_token is None:
            break

    df = pd.DataFrame(all_reviews[:num_reviews])
    print(df.columns)
    return df


def save_reviews_to_csv(df: pd.DataFrame, path: str = "data/cleaned_reviews.csv"):
    """
    Save the DataFrame of reviews to a CSV file.
    """
    df.to_csv(path, index=False)
    print(f" Reviews saved to {path}")
