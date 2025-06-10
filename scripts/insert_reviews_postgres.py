import pandas as pd
import psycopg2

df = pd.read_csv("data/sentiment_themes.csv")

conn = psycopg2.connect(
    dbname="bank_reviews", user="bankuser", password="bankpass", host="localhost"
)
cur = conn.cursor()

# Insert banks
bank_ids = {}
for bank in df["bank"].unique():
    cur.execute(
        "INSERT INTO banks (name) VALUES (%s) ON CONFLICT (name) DO NOTHING RETURNING id",
        (bank,),
    )
    result = cur.fetchone()
    if result:
        bank_ids[bank] = result[0]
    else:
        cur.execute("SELECT id FROM banks WHERE name = %s", (bank,))
        bank_ids[bank] = cur.fetchone()[0]

# Insert reviews
for _, row in df.iterrows():
    cur.execute(
        """
        INSERT INTO reviews (review_text, rating, review_date, sentiment_label, sentiment_score, identified_theme, bank_id)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
    """,
        (
            row["review"],
            int(row["rating"]),
            row["date"],
            row["sentiment_label"],
            float(row["sentiment_score"]),
            row["identified_theme"],
            bank_ids[row["bank"]],
        ),
    )

conn.commit()
conn.close()
