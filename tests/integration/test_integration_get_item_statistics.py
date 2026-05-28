import pytest

from light_artifactory_client.responses import GetItemStatisticsResponse

pytestmark = pytest.mark.integration

class TestIntegrationGetItemStatistics:
    def test_integration_get_item_statistics_success(self, integration_client, deployed_artifact):
        repo, path = deployed_artifact
        result = integration_client.get_item_statistics(repo, path)
        assert isinstance(result, GetItemStatisticsResponse)
        assert result.status_code == 200
