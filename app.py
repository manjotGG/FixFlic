from flask import Flask, render_template, request
from movie_recommender import recommend_movie

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/recommend", methods=["POST"])
def recommend():
    mood = int(request.form.get("mood"))
    genre = int(request.form.get("genre"))
    year_pref = int(request.form.get("year_pref"))
    movie = recommend_movie(mood, genre, year_pref)
    return render_template("result.html", movie=movie)

if __name__ == "__main__":
    app.run(debug=True)
