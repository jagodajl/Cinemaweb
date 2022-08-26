from flask import Flask, render_template, request

import tmdb_client

app = Flask(__name__)


@app.route('/')
def homepage():
    list_selection = ["popular", "upcoming", "top_rated", "now_playing"]
    selected_list = request.args.get('list_type')

    if selected_list in list_selection:
        movies = tmdb_client.get_popular_movies_n(8, selected_list)
        return render_template("homepage.html", movies=movies, current_list=selected_list,
                               list_selection=list_selection)
    else:
        selected_list = "popular"
        movies = tmdb_client.get_popular_movies_n(8, selected_list)
        return render_template("homepage.html", movies=movies, current_list=selected_list, list_selection=list_selection)


@app.route("/movie/<movie_id>")
def movie_details(movie_id):
    details = tmdb_client.get_single_movie(movie_id)
    cast = tmdb_client.get_single_movie_cast(20, movie_id)
    return render_template("movie_details.html", movie=details, cast=cast)


@app.context_processor
def utility_processor():
    def tmdb_image_url(path, size):
        return tmdb_client.get_poster_url(path, size)

    return {"tmdb_image_url": tmdb_image_url}


if __name__ == '__main__':
    app.run(debug=True)
