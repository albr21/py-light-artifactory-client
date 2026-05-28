import pytest

from light_artifactory_client import NotFoundError
from light_artifactory_client.responses import ListItemsResponse

pytestmark = pytest.mark.integration

class TestIntegrationListItems:
    def test_integration_list_items_success(self, integration_client, deployed_artifact):
        repo, _ = deployed_artifact
        result = integration_client.list_items(repo)
        assert isinstance(result, ListItemsResponse)
        assert result.status_code == 200

    def test_integration_list_items_deep(self, integration_client, deployed_artifact):
        repo, _ = deployed_artifact
        result = integration_client.list_items(repo, deep=True)
        assert isinstance(result, ListItemsResponse)

    def test_integration_list_items_not_found(self, integration_client, integration_repo):
        with pytest.raises(NotFoundError):
            integration_client.list_items("nonexistent-repo-xyz")
