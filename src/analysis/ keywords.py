from sklearn.feature_extraction.text import TfidfVectorizer


def extract_keywords(corpus, top_n=100):
    vectorizer = TfidfVectorizer(
        stop_words="english", ngram_range=(1, 2), max_features=top_n
    )
    X = vectorizer.fit_transform(corpus)
    return vectorizer.get_feature_names_out()
