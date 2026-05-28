import pytest

from light_artifactory_client import NotFoundError
from light_artifactory_client.responses import DeleteItemResponse

pytestmark = pytest.mark.integration

class TestIntegrationDeleteItem:
    def test_integration_delete_item_success(self, integration_client, integration_repo):
        integration_client.deploy_artifact(
            integration_repo, "to-delete.txt", b"bye"
        )
        result = integration_client.delete_item(integration_repo, "to-delete.txt")
        assert isinstance(result, DeleteItemResponse)
        assert result.status_code == 204

    def test_integration_delete_item_not_found(self, integration_client, integration_repo):
        with pytest.raises(NotFoundError):
            integration_client.delete_item(integration_repo, "nonexistent/file.txt")
