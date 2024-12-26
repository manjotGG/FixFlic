import requests
import random

API_KEY = "fd75f2cbedc1bf37544712100425c13f"
BASE_URL = "https://api.themoviedb.org/3"

def get_popular_movies():
    url = f"{BASE_URL}/movie/popular"
    params = {"api_key": API_KEY, "language": "en-US", "page": 1}
    response = requests.get(url, params=params)
    data = response.json()
    return data.get("results", [])

def recommend_movie(mood, genre, year_pref):
    movies = get_popular_movies()
    if not movies:
        return "No movies available at the moment."
    
    # Filter based on inputs (you can enhance this logic further)
    filtered_movies = movies
    if year_pref == 2:
        filtered_movies = [m for m in movies if int(m["release_date"][:4]) < 2000]
    elif year_pref == 3:
        filtered_movies = [m for m in movies if int(m["release_date"][:4]) >= 2020]

    if genre == 1:  # Comedy
        filtered_movies = [m for m in filtered_movies if "Comedy" in m.get("genre_ids", [])]

    return random.choice(filtered_movies)["title"] if filtered_movies else "No matching movies found."
