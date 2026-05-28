import pytest

from light_artifactory_client import NotFoundError
from light_artifactory_client.responses import RetrieveArtifactResponse

from .conftest import ARTIFACT_CONTENT

pytestmark = pytest.mark.integration

class TestIntegrationRetrieveArtifact:
    def test_integration_retrieve_artifact_success(self, integration_client, deployed_artifact):
        repo, path = deployed_artifact
        result = integration_client.retrieve_artifact(repo, path)
        assert isinstance(result, RetrieveArtifactResponse)
        assert result.body == ARTIFACT_CONTENT.decode()

    def test_integration_retrieve_artifact_not_found(self, integration_client, integration_repo):
        with pytest.raises(NotFoundError):
            integration_client.retrieve_artifact(integration_repo, "nonexistent/file.txt")
