import sys
import os
import pandas as pd

# Ensure src/ is in the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))


# scripts/scrape_reviews.py
from preprocessing import preprocess_reviews
from screapmodule import scrape_reviews, save_reviews_to_csv
import pandas as pd

apps = {
    "Dashen Bank": "com.dashen.dashensuperapp",
    "Commercial Bank of Ethiopia": "com.combanketh.mobilebanking",
    "Bank of Abyssinia": "com.boa.boaMobileBanking",
}

all_reviews = []

for bank, app_id in apps.items():
    print(f"Scraping {bank}...")
    df = scrape_reviews(app_id=app_id, bank_name=bank, num_reviews=500)
    df = preprocess_reviews(df)
    all_reviews.append(df)

combined_df = pd.concat(all_reviews, ignore_index=True)
save_reviews_to_csv(combined_df)
print("✅ All reviews saved to data/cleaned_reviews.csv")
