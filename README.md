# Bank App Review Analysis

This project analyzes Google Play Store reviews for three major Ethiopian banks to support product, marketing, and engineering insights.

## Project Overview

This project analyzes user reviews of three major Ethiopian banking apps—Dashen Bank, Commercial Bank of Ethiopia (CBE), and Bank of Abyssinia (BOA)—from the Google Play Store.  
The goal is to extract insights for product, marketing, and engineering teams to enhance user experience, feature offerings, and customer support efficiency.

## Project Structure

bank-app-review-analysis/
.github/workflows/ # GitHub Actions workflows
unittests.yml
.vscode/ # Optional IDE settings
data/ # Raw and cleaned data
notebooks/ # Jupyter notebooks for EDA and modeling
scripts/ # Script entry points (scraper, etc.)
src/ # Core logic and modular code
scraper/ # Web scraping and preprocessing modules
tests/ # Unit tests
requirements.txt # Project dependencies
README.md # Project overview
.gitignore
How to Run

1. Clone the Repo
   git clone https://github.com/bethel4/bank-app-review-analysis.git
   cd bank-app-review-analysis
2. Create Virtual Environment
   python -m venv venv
   source venv/bin/activate # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
3. Scrape and Preprocess Reviews
   python scripts/scrape_reviews.py
   This saves the cleaned reviews to data/cleaned_reviews.csv.
