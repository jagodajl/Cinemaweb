from unittest.mock import Mock

import pytest

import tmdb_client
from main import app


def should_fetch_poster_size():
    poster_api_path = "some-poster-path"
    expected_default_size = 'w342'
    poster_url = tmdb_client.get_poster_url(poster_api_path=poster_api_path, size=expected_default_size)
    assert expected_default_size in poster_url


def should_fetch_not_empty_object_for_list_type():
    movies_list = tmdb_client.get_list_type_movies(list_type="popular")
    assert movies_list is not None


@pytest.mark.parametrize("list_type", ("top_rated", "upcoming", "popular", "now_playing"))
def should_check_if_the_button_is_active(monkeypatch, list_type):
    api_mock = Mock(return_value={"results": []})
    monkeypatch.setattr("tmdb_client._call_get_api", api_mock)
    expected_html_cut_off = f"href=\"/?list_type={list_type}\" class=\"btn btn-outline-info active\""
    with app.test_client() as client:
        response = client.get(f"/?list_type={list_type}")
        assert response.status_code == 200
        html = str(response.get_data())
        count = html.count(expected_html_cut_off)
        assert count == 1


def should_fetch_not_empty_object_for_movie_cast():
    mock_single_movie_cast = "Strike"
    cast = tmdb_client._get_single_movie_cast_call(movie_id=mock_single_movie_cast)
    assert cast is not None


def should_get_expected_movie_by_id(monkeypatch):
    mock_single_movie_id = "11111"
    single_movie_mock = Mock()
    single_movie_mock.return_value = mock_single_movie_id
    monkeypatch.setattr("tmdb_client.get_single_movie", single_movie_mock)
    single_movie = tmdb_client.get_single_movie(mock_single_movie_id)
    assert single_movie == mock_single_movie_id
