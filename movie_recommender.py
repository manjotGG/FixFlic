import requests
import random

API_KEY = "fd75f2cbedc1bf37544712100425c13f"
BASE_URL = "https://api.themoviedb.org/3"

quiz = [
    {"question": "How is your mood today?", "options": ["Happy", "Normal", "Sad"]},
    {"question": "What kind of movie do you like?", "options": ["Comedy", "Action", "Comedy Romance"]},
    {"question": "Do you have any year preference?", "options": ["No Preference", "Late 90s", "Latest"]},
]

GENRE_MAP = {
    1: 35,  # Comedy
    2: 28,  # Action
    3: 10749,  # Comedy Romance
}

YEAR_MAP = {
    1: None,  # No year preference
    2: (1990, 2000),  # Late 90s
    3: (2015, 2024),  # Latest
}

def recommend_movie(genre_choice, year_choice):
    genre_id = GENRE_MAP.get(genre_choice)
    year_range = YEAR_MAP.get(year_choice)

    url = f"{BASE_URL}/discover/movie"
    params = {
        "api_key": API_KEY,
        "language": "en-US",
        "sort_by": "popularity.desc",
        "with_genres": genre_id,
        "primary_release_date.gte": f"{year_range[0]}-01-01" if year_range else None,
        "primary_release_date.lte": f"{year_range[1]}-12-31" if year_range else None,
        "page": 1,
    }
    params = {k: v for k, v in params.items() if v is not None}  # Remove None values

    response = requests.get(url, params=params)
    if response.status_code != 200:
        return f"Error: Unable to fetch movies (status code {response.status_code})"

    data = response.json()
    movies = data.get("results", [])
    if not movies:
        return None  # No matching movies found

    # Pick a random movie from the results
    return random.choice(movies)
