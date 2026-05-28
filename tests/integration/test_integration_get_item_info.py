import pytest

from light_artifactory_client import NotFoundError
from light_artifactory_client.responses import GetItemInfoResponse

pytestmark = pytest.mark.integration

class TestIntegrationGetItemInfo:
    def test_integration_get_item_info_success(self, integration_client, deployed_artifact):
        repo, path = deployed_artifact
        result = integration_client.get_item_info(repo, path)
        assert isinstance(result, GetItemInfoResponse)
        assert result.status_code == 200

    def test_integration_get_item_info_not_found(self, integration_client, integration_repo):
        with pytest.raises(NotFoundError):
            integration_client.get_item_info(integration_repo, "nonexistent/path/file.txt")
