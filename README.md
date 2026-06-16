# Movie Recommendation System

A content-based Movie Recommendation System built using Python, Machine Learning, Streamlit, and the TMDB API.

This project recommends similar movies by analyzing genres, keywords, cast, crew, and movie overviews using TF-IDF Vectorization and Cosine Similarity.


## Features

* Movie recommendations based on content similarity
* Fuzzy movie search support
* Movie posters fetched from TMDB API
* Movie ratings and release dates
* Match percentage display
* Dark-themed Streamlit interface
* Genre-based recommendation filtering


## Tech Stack

* Python
* Pandas
* Scikit-Learn
* TF-IDF Vectorizer
* Cosine Similarity
* Streamlit
* TMDB API
* Git & GitHub

## Dataset

This project uses the TMDB 5000 Movies Dataset.

Files used:

* `tmdb_5000_movies.csv`
* `tmdb_5000_credits.csv`


## How Recommendations Are Generated

1. Merge movie and credits datasets
2. Extract genres, keywords, cast, and crew information
3. Perform text preprocessing and feature engineering
4. Generate movie tags
5. Apply TF-IDF Vectorization
6. Calculate similarity using Cosine Similarity
7. Filter and rank recommendations


## Installation

Clone the repository:

bash
git https://github.com/ARTTIC25/movierecommendation.git
cd movierecommendation

Install dependencies:

bash
pip install -r requirements.txt

Create a `.env` file:
env
API_KEY=YOUR_TMDB_API_KEY

Run the application:

bash
streamlit run app.py


## Project Structure


movierecommendation/
│
├── app.py
├── train.py
├── movies.pkl
├── requirements.txt
├── .gitignore
├── README.md
├── tmdb_5000_movies.csv
└── tmdb_5000_credits.csv


## Learning Outcomes

Through this project I learned:

* Data preprocessing
* Feature engineering
* Natural Language Processing basics
* TF-IDF Vectorization
* Cosine Similarity
* API integration
* Streamlit application development
* Git and GitHub workflow
* Deployment preparation

## Author
Amith P Anil
B.Tech Data Science Student

## Disclaimer
This project was created for educational and learning purposes.
Movie data and poster assets are provided by TMDB.
