# FixFlic - Movie Recommendation Web App

FixFlic is a movie recommendation web app that suggests movies based on user preferences and mood. The app uses the TMDb API to fetch movie data and recommends movies based on a short quiz to understand the user's mood and movie preferences.

## Features
- Interactive quiz to understand the user's mood and movie preferences.
- Personalized movie recommendations based on quiz results.
- View detailed information about the recommended movies (e.g., title, release date, overview, poster).
- Take the quiz again to get new recommendations.

## Technologies Used
- **Flask**: Backend framework to handle HTTP requests and responses.
- **Jinja2**: Templating engine used for rendering HTML pages.
- **TMDb API**: API used to fetch movie data.
- **HTML/CSS**: Frontend structure and styling.
- **Python**: Backend logic and movie recommendation processing.

## Installation

1. Clone this repository to your local machine:
    ```bash
    git clone https://github.com/your-username/fixflic.git
    ```

2. Navigate to the project directory:
    ```bash
    cd fixflic
    ```

3. Create a virtual environment:
    ```bash
    python3 -m venv venv
    ```

4. Activate the virtual environment:
    - On Windows:
        ```bash
        venv\Scripts\activate
        ```
    - On Mac/Linux:
        ```bash
        source venv/bin/activate
        ```

5. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

6. Run the application:
    ```bash
    python app.py
    ```

7. Visit `http://127.0.0.1:5000` in your browser to access the web app.

## Project Structure
- **app.py**: The main file for Flask application routes.
- **movie_recommender.py**: Contains the logic for movie recommendations based on quiz answers.
- **templates/**: Contains all the HTML templates used by Flask.
- **static/**: Contains static files like images, CSS, and JavaScript.

## Contributors
- **ManjotGG** - Main Developer
- **AbhigyanGG** - Contributor

## Acknowledgements
- [TMDb API](https://www.themoviedb.org/) for providing movie data.
