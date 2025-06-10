CREATE TABLE banks (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) UNIQUE NOT NULL
);

CREATE TABLE reviews (
    id SERIAL PRIMARY KEY,
    review_text TEXT,
    rating INTEGER,
    review_date DATE,
    sentiment_label VARCHAR(20),
    sentiment_score FLOAT,
    identified_theme VARCHAR(100),
    bank_id INTEGER REFERENCES banks(id)
);
