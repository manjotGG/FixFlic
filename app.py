from flask import Flask, render_template, request
from movie_recommender import quiz, recommend_movie
from movie_recommender import get_movie_details, get_watch_providers


app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html", quiz=quiz)

@app.route("/submit_quiz", methods=["POST"])
def submit_quiz():
    # Retrieve user responses
    mood = int(request.form.get("mood"))
    genre = int(request.form.get("genre"))
    year = int(request.form.get("year"))

    # Fetch recommended movie
    movie = recommend_movie(genre, year)
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
