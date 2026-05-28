import os
import pytest

from .conftest import ARTIFACT_CONTENT

pytestmark = pytest.mark.integration

class TestIntegrationRetrieveArtifactUsingUri:
    def test_integration_retrieve_using_uri_success(self, integration_client, deployed_artifact):
        repo, path = deployed_artifact
        host = os.environ.get("ARTIFACTORY_URL", "http://localhost:8081/artifactory").rstrip("/")
        uri = f"{host}/artifactory/{repo}/{path}"
        result = integration_client.retrieve_artifact_using_uri(uri)
        assert result.body == ARTIFACT_CONTENT.decode()
