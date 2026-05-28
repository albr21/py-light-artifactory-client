import pytest

from light_artifactory_client.responses import DeployArtifactResponse

pytestmark = pytest.mark.integration

class TestIntegrationDeployArtifact:
    def test_integration_deploy_artifact_success(self, integration_client, integration_repo):
        result = integration_client.deploy_artifact(
            integration_repo,
            "deploy-test.txt",
            b"hello",
        )
        assert isinstance(result, DeployArtifactResponse)
        assert result.status_code == 201
        integration_client.delete_item(integration_repo, "deploy-test.txt")

    def test_integration_deploy_artifact_with_properties(self, integration_client, integration_repo):
        result = integration_client.deploy_artifact(
            integration_repo,
            "deploy-with-props.txt",
            b"data",
            properties={"env": "test", "version": "1.0"},
        )
        assert isinstance(result, DeployArtifactResponse)
        integration_client.delete_item(integration_repo, "deploy-with-props.txt")
