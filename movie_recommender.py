import requests
import random

TMDB_API_KEY = "fd75f2cbedc1bf37544712100425c13f"
BASE_URL = "https://api.themoviedb.org/3"
API_KEY = TMDB_API_KEY

quiz = [
    {"question": "How is your mood today?", "options": ["Happy", "Normal", "Sad"]},
    {"question": "What kind of movie do you like?", "options": ["Comedy", "Action", "Comedy Romance"]},
    {"question": "Do you have any year preference?", "options": ["No Preference", "Late 90s", "Latest"]},
]

GENRE_MAP = {
    1: 35,  
    2: 28, 
    3: 10749,  
}

YEAR_MAP = {
    1: None,  
    2: (1990, 2000),  
    3: (2015, 2024),  
}

def recommend_movie(genre_choice, year_choice, mood_score):
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
    params = {k: v for k, v in params.items() if v is not None}  

    response = requests.get(url, params=params)
    if response.status_code != 200:
        return f"Error: Unable to fetch movies (status code {response.status_code})"

    data = response.json()
    movies = data.get("results", [])
    if not movies:
        return None  # No matching movies found

    # Pick a random movie from the results
    return random.choice(movies)

def get_movie_details(movie_id):
    """Fetch movie details from TMDb."""
    url = f"https://api.themoviedb.org/3/movie/{movie_id}"
    response = requests.get(url, params={"api_key": API_KEY})
    if response.status_code == 200:
        return response.json()
    return None

# Mapping of provider names to URLs
PROVIDER_URLS = {
    "Netflix": "https://www.netflix.com",
    "Amazon Prime Video": "https://www.amazon.com/Prime-Video",
    "Disney+": "https://www.disneyplus.com",
    "Hulu": "https://www.hulu.com",
    "Apple TV+": "https://www.apple.com/tv/",
    "Google Play Movies": "https://play.google.com/store/movies",
    "iTunes": "https://www.apple.com/itunes",
    "YouTube": "https://www.youtube.com",
    
}

def get_watch_providers(movie_id):
    """Fetch watch providers for a movie from TMDb API."""
    url = f"https://api.themoviedb.org/3/movie/{movie_id}/watch/providers"
    params = {"api_key": TMDB_API_KEY}
    
    response = requests.get(url, params=params)
    
    if response.status_code != 200:
        return {"streaming": [], "rent": [], "buy": []}
    
    data = response.json()
    results = data.get("results", {})
    
    region = results.get("US") or results.get("IN")  

    if not region:
        return {"streaming": [], "rent": [], "buy": []}

    
    providers = {
        "streaming": [(item["provider_name"], PROVIDER_URLS.get(item["provider_name"], "#")) for item in region.get("flatrate", [])],
        "rent": [(item["provider_name"], PROVIDER_URLS.get(item["provider_name"], "#")) for item in region.get("rent", [])],
        "buy": [(item["provider_name"], PROVIDER_URLS.get(item["provider_name"], "#")) for item in region.get("buy", [])],
    }

    return providers
