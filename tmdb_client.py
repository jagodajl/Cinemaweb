import requests


def _call_get_api(path):
    url = f"https://api.themoviedb.org/3/{path}"
    return requests.get(url, headers=_get_auth_header()).json()


def _call_get_api_variable(path, variable):
    url = f"https://api.themoviedb.org/3/{path}/{variable}"
    return requests.get(url, headers=_get_auth_header()).json()


def _call_get_api_cast_variable(path, variable, path2):
    url = f"https://api.themoviedb.org/3/{path}/{variable}/{path2}"
    return requests.get(url, headers=_get_auth_header()).json()


def _get_auth_header():
    api_token = "eyJhbGciOiJIUzI1NiJ9" \
                ".eyJhdWQiOiJjOGFhNTdkNDY3NTE2OGY2NGJkYWRlODViZWMwMzhmMCIsInN1YiI6IjYyZjM3N2ZkZmVhNmUzMDA5MTM1YTMzZiIs" \
                "InNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.wKtKqJPk_95ggEMzRC2l_hrjZ9pOhuRW1z32FFqyHwg "

    return {"Authorization": f"Bearer {api_token}"}


def get_poster_url(poster_api_path, size):
    base_url = "https://image.tmdb.org/t/p/"
    return f"{base_url}{size}/{poster_api_path}"


def get_popular_movies():
    return _call_get_api("movie/popular")


def get_popular_movies_n(how_many):
    data = get_popular_movies()
    return data["results"][:how_many]


def get_single_movie(movie_id):
    return _call_get_api_variable("movie", movie_id)


def get_single_movie_cast_call(movie_id):
    return _call_get_api_cast_variable("movie", movie_id, "credits")


def get_single_movie_cast(movie_id):
    data = get_single_movie_cast_call(movie_id)
    return data["cast"]
