from flask import Flask, render_template, request
from movie_recommender import quiz, recommend_movie
from movie_recommender import get_movie_details, get_watch_providers


app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html", quiz=quiz)

@app.route('/makers')
def makers():
    return render_template('makers.html')

@app.route("/submit_quiz", methods=["POST"])
def submit_quiz():
    # Retrieve user responses
    mood = request.form.get("mood")  # 'happy', 'sad', 'neutral'
    genre = request.form.get("genre")  # 'comedy', 'action', etc.
    year = request.form.get("year")  # Year or range like '2020s'

    # Optional: Map mood to a numeric value if needed for recommendation
    mood_score = None
    if mood == 'happy':
        mood_score = 1
    elif mood == 'sad':
        mood_score = 2
    elif mood == 'neutral':
        mood_score = 3

    # Optional: Map genre to a numeric value if needed for recommendation
    genre_mapping = {
        'comedy': 1,
        'action': 2,
        'drama': 3,
        'romance': 4,
        'horror': 5,
        'thriller': 6,
        'sci-fi': 7,
        # Add other genres as necessary
    }
    
    genre_id = genre_mapping.get(genre, None)  # Default to None if genre is not in mapping

    # Handle year input, checking if it's a range
    if 's' in year:  # For cases like '2020s', '2010s'
        base_year = int(year[:4])  # Get the base year (e.g., '2020' from '2020s')
        year = base_year  # You could also decide to pick a middle year or a default year from the range
    else:
        try:
            year = int(year)  # If it's a specific year, try to convert it to int
        except ValueError:
            year = 2020  # Fallback to a default year if conversion fails

    # Fetch recommended movie based on genre, year, and mood_score
    movie = recommend_movie(genre_id, year, mood_score)  # Pass genre_id and mood_score to recommendation logic
    if movie:
        # Get watch providers for the recommended movie
        providers = get_watch_providers(movie["id"]) if "id" in movie else {"streaming": [], "rent": [], "buy": []}
        
        return render_template(
            "result.html",
            title=movie["title"],
            release_date=movie.get("release_date", "Unknown"),
            overview=movie.get("overview", "No overview available."),
            poster_path=f"https://image.tmdb.org/t/p/w500{movie['poster_path']}" if movie.get("poster_path") else None,
            providers=providers,  # Pass providers to the template
        )
    else:
        return render_template("result.html", error="No movies match your criteria. Please try again!")


@app.route('/result/<movie_id>')
def result(movie_id):
    """Display the result page with movie details and watch providers."""
    movie = get_movie_details(movie_id)
    if not movie:
        return render_template("result.html", error="Movie not found!")

    # Fetch providers
    providers = get_watch_providers(movie_id)
    
    # Prepare movie details
    movie_data = {
        "title": movie.get("title"),
        "release_date": movie.get("release_date"),
        "overview": movie.get("overview"),
        "poster_path": f"https://image.tmdb.org/t/p/w500{movie.get('poster_path')}" if movie.get("poster_path") else None
    }

    return render_template("result.html", **movie_data, providers=providers)
@app.context_processor
def utility_processor():
    return {"enumerate": enumerate}


if __name__ == "__main__":
    app.run(debug=True)
