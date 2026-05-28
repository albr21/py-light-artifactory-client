import pytest

from light_artifactory_client.exceptions import AlreadyConnectedError

SERVER_URL = "https://artifactory.example.com"

class TestClientLogin:
    def test_client_login_sets_credentials(self, client):
        client.login("username", "password")
        assert client.username == "username"
        assert client.password == "password"
        assert client.is_logged is True

    def test_client_login_sets_session_auth(self, client):
        client.login("username", "password")
        assert client.session.auth == ("username", "password")

    def test_client_login_twice_raises(self, client):
        client.login("username", "password")
        with pytest.raises(AlreadyConnectedError):
            client.login("username2", "password2")

    def test_client_login_force_replaces_credentials(self, client):
        client.login("username", "password")
        client.login("username2", "password2", force=True)
        assert client.username == "username2"
        assert client.password == "password2"

    def test_client_logout_clears_credentials(self, client):
        client.login("username", "password")
        client.logout()
        assert client.username is None
        assert client.password is None
        assert client.is_logged is False

    def test_client_logout_clears_session_auth(self, client):
        client.login("username", "password")
        client.logout()
        assert client.session.auth is None

    def test_client_login_logout_login_cycle(self, client):
        client.login("username", "password")
        client.logout()
        client.login("username2", "password2")
        assert client.username == "username2"
        assert client.password == "password2"
