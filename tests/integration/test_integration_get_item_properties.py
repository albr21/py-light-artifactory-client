import pytest

from light_artifactory_client import NotFoundError
from light_artifactory_client.responses import GetItemPropertiesResponse

pytestmark = pytest.mark.integration

class TestIntegrationGetItemProperties:
    def test_integration_get_item_properties_success(self, integration_client, deployed_artifact):
        repo, path = deployed_artifact
        result = integration_client.get_item_properties(repo, path)
        assert isinstance(result, GetItemPropertiesResponse)
        assert result.status_code == 200

    def test_integration_get_item_properties_not_found(self, integration_client, integration_repo):
        with pytest.raises(NotFoundError):
            integration_client.get_item_properties(integration_repo, "nonexistent/file.txt")
