from flask import Flask, render_template

import tmdb_client

app = Flask(__name__)


# @app.route('/')
# def homepage():
#     return render_template("index.html")

@app.route('/')
def homepage():
    popular_movies = tmdb_client.get_popular_movies_n(8)
    return render_template("homepage.html", movies=popular_movies)


@app.route("/movie/<movie_id>")
def movie_details(movie_id):
    details = tmdb_client.get_single_movie("766507")
    cast = tmdb_client.get_single_movie_cast("766507")
    print(cast)
    return render_template("movie_details.html", movie=details)


@app.context_processor
def utility_processor():
    def tmdb_image_url(path):
        return tmdb_client.get_poster_url(path, "w342")

    return {"tmdb_image_url": tmdb_image_url}


@app.context_processor
def utility_processor_backdrop_path():
    def tmdb_image_url(path):
        return tmdb_client.get_poster_url(path, "w780")

    return {"tmdb_image_url": tmdb_image_url}


if __name__ == '__main__':
    app.run(debug=True)
