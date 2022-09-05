from unittest.mock import Mock

import pytest

import tmdb_client
from main import app


def test_get_poster_url():
    poster_api_path = "some-poster-path"
    expected_default_size = 'w342'
    poster_url = tmdb_client.get_poster_url(poster_api_path=poster_api_path, size=expected_default_size)
    assert expected_default_size in poster_url


def test_get_movies_list_type_popular():
    movies_list = tmdb_client.get_list_type_movies(list_type="popular")
    assert movies_list is not None


@pytest.mark.parametrize("list_type", ("top_rated", "upcoming", "popular", "now_playing"))
def test_movies_list(monkeypatch, list_type):
    api_mock = Mock(return_value={"results": []})
    monkeypatch.setattr("tmdb_client._call_get_api", api_mock)

    with app.test_client() as client:
        response = client.get("/")
        assert response.status_code == 200


def test_get_single_movie_cast():
    mock_single_movie_cast = "Strike"
    cast = tmdb_client._get_single_movie_cast_call(movie_id=mock_single_movie_cast)
    assert cast is not None


def test_get_single_movie(monkeypatch):
    mock_single_movie_id = "11111"
    single_movie_mock = Mock()
    single_movie_mock.return_value = mock_single_movie_id
    monkeypatch.setattr("tmdb_client.get_single_movie", single_movie_mock)
    single_movie = tmdb_client.get_single_movie(mock_single_movie_id)
    assert single_movie == mock_single_movie_id
