def assign_theme(text):
    themes = {
        "Account Access Issues": [
            "login",
            "password",
            "pin",
            "authentication",
            "blocked",
            "locked",
        ],
        "Transaction Performance": [
            "transfer",
            "transaction",
            "slow",
            "failed",
            "processing",
        ],
        "User Interface & Experience": [
            "interface",
            "navigation",
            "layout",
            "design",
            "ui",
        ],
        "Customer Support": ["support", "help", "agent", "contact", "response"],
        "Feature Requests": [
            "feature",
            "fingerprint",
            "face",
            "add",
            "request",
            "option",
        ],
        "Stability & Reliability": [
            "crash",
            "bug",
            "freeze",
            "hang",
            "issue",
            "glitch",
        ],
        "Positive Feedback": [
            "good",
            "great",
            "excellent",
            "love",
            "perfect",
            "amazing",
        ],
    }

    text = text.lower()
    for theme, keywords in themes.items():
        for word in keywords:
            if word in text:
                return theme
    return "Other"


def extract_themes(df):
    df["identified_theme"] = df["review"].apply(assign_theme)
    return df
