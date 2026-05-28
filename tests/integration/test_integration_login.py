import os
import pytest

from light_artifactory_client import ArtifactoryClient, NotAuthenticatedError
from light_artifactory_client.exceptions import AlreadyConnectedError

pytestmark = pytest.mark.integration

class TestIntegrationLogin:
    def test_integration_login_invalid_credentials(self, integration_client):
        host = os.environ.get("ARTIFACTORY_URL", "http://localhost:8081/artifactory")
        bad_client = ArtifactoryClient(host, username="wrong", password="wrong")
        with pytest.raises(NotAuthenticatedError):
            bad_client.get_item_info("any-repo", "any/path")

    def test_integration_login_already_connected_raises(self, integration_client):
        with pytest.raises(AlreadyConnectedError):
            integration_client.login("user2", "pass2")

    def test_integration_login_force(self, integration_client):
        host = os.environ.get("ARTIFACTORY_URL", "http://localhost:8081/artifactory")
        temp = ArtifactoryClient(host, username=integration_client.username, password=integration_client.password)
        temp.login("anotheruser", "anotherpass", force=True)
        assert temp.username == "anotheruser"
