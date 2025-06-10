import psycopg2
import pandas as pd

# Load processed data
df = pd.read_csv("data/sentiment_themes.csv")

# Connect to PostgreSQL
conn = psycopg2.connect(
    dbname="bank_reviews",
    user="bankuser",
    password="bankpass",
    host="localhost",
    port="5432",
)
cur = conn.cursor()

# Insert unique banks
banks = df["bank"].unique()
bank_map = {}

for bank in banks:
    cur.execute(
        "INSERT INTO banks (name) VALUES (%s) ON CONFLICT (name) DO NOTHING RETURNING id;",
        (bank,),
    )
    conn.commit()
    cur.execute("SELECT id FROM banks WHERE name = %s", (bank,))
    bank_id = cur.fetchone()[0]
    bank_map[bank] = bank_id

# Insert reviews
for _, row in df.iterrows():
    cur.execute(
        """
        INSERT INTO reviews (review, rating, review_date, source, sentiment_label, sentiment_score, theme, bank_id)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
    """,
        (
            row["review"],
            int(row["rating"]),
            row["date"],
            row["source"],
            row["sentiment_label"],
            float(row["sentiment_score"]),
            row["identified_theme"],
            bank_map[row["bank"]],
        ),
    )

conn.commit()
cur.close()
conn.close()
print("Data inserted successfully.")
