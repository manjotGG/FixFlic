import requests
import random

API_KEY = "fd75f2cbedc1bf37544712100425c13f"
BASE_URL = "https://api.themoviedb.org/3"

def Suprise_me():
    url = f"{BASE_URL}/movie/popular"  # Corrected endpoint
    params = {"api_key": API_KEY, "language": "en-US", "page": 1}
    response = requests.get(url, params=params)
    data = response.json()
    movie = data.get("results",[])
    if movie:
        random_movie = random.choice(movie)
        return f"{random_movie['title']} ({random_movie['release_date'][:4]})"
    else:
        return f"Error:"

movie = Suprise_me()
print("Popular Movies:", movie)
print("helloworld")