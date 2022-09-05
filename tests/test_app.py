from main import app
from unittest.mock import Mock


def test_homepage(monkeypatch):
    api_mock = Mock(return_value={"results": []})
    monkeypatch.setattr("tmdb_client.get_list_type_movies", api_mock)

    with app.test_client() as client:
        response = client.get("/")
        assert response.status_code == 200
        api_mock.assert_called_once_with("popular")
