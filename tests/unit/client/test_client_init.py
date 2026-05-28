from light_artifactory_client import ArtifactoryClient

SERVER_URL = "https://artifactory.example.com"

class TestClientInit:
    def test_client_init_host_trailing_slash(self):
        client = ArtifactoryClient(SERVER_URL)
        assert client.host == SERVER_URL + "/"

    def test_client_init_host_already_has_trailing_slash(self):
        client = ArtifactoryClient(SERVER_URL + "/")
        assert client.host == SERVER_URL + "/"

    def test_client_init_default_timeout(self):
        client = ArtifactoryClient(SERVER_URL)
        assert client.timeout == 60.0

    def test_client_init_custom_timeout(self):
        client = ArtifactoryClient(SERVER_URL, timeout=30.0)
        assert client.timeout == 30.0

    def test_client_init_default_max_retries(self):
        client = ArtifactoryClient(SERVER_URL)
        assert client.max_retries == 3

    def test_client_init_default_retry_backoff_factor(self):
        client = ArtifactoryClient(SERVER_URL)
        assert client.retry_backoff_factor == 0.5

    def test_client_init_not_logged_by_default(self):
        client = ArtifactoryClient(SERVER_URL)
        assert client.is_logged is False
        assert client.username is None
        assert client.password is None

    def test_client_init_session_not_authenticated_by_default(self):
        client = ArtifactoryClient(SERVER_URL)
        assert client.session.auth is None

    def test_client_init_logged_with_credentials(self):
        client = ArtifactoryClient(SERVER_URL, username="user", password="pass")
        assert client.is_logged is True
        assert client.username == "user"
        assert client.password == "pass"

    def test_client_init_session_auth_set_with_credentials(self):
        client = ArtifactoryClient(SERVER_URL, username="user", password="pass")
        assert client.session.auth == ("user", "pass")
