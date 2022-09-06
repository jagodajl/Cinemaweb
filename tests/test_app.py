import pytest

from main import app
from unittest.mock import Mock


@pytest.mark.parametrize("list_type", ("top_rated", "upcoming", "popular", "now_playing"))
def test_homepage(monkeypatch, list_type):
    api_mock = Mock(return_value={"results": []})
    monkeypatch.setattr("tmdb_client.get_list_type_movies", api_mock)

    with app.test_client() as client:
        response = client.get(f"/?list_type={list_type}")
        assert response.status_code == 200
        api_mock.assert_called_once_with(list_type)
