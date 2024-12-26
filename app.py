from flask import Flask, render_template, request
from movie_recommender import quiz, recommend_movie

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
        return render_template(
            "result.html",
            title=movie["title"],
            release_date=movie.get("release_date", "Unknown"),
            overview=movie.get("overview", "No overview available."),
            poster_path=f"https://image.tmdb.org/t/p/w500{movie['poster_path']}" if movie.get("poster_path") else None,
        )
    else:
        return render_template("result.html", error="No movies match your criteria. Please try again!")

@app.context_processor
def utility_processor():
    return {"enumerate": enumerate}


if __name__ == "__main__":
    app.run(debug=True)
