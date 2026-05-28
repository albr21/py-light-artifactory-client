import pytest

from light_artifactory_client.responses import SearchItemsByPropertiesResponse

pytestmark = pytest.mark.integration

class TestIntegrationSearchItemsByProperties:
    def test_integration_search_by_properties_success(self, integration_client, deployed_artifact):
        repo, _ = deployed_artifact
        result = integration_client.search_items_by_properties(
            {"test.source": "integration"}, repos=repo
        )
        assert isinstance(result, SearchItemsByPropertiesResponse)
        assert len(result.results) >= 1

    def test_integration_search_by_properties_with_detail(self, integration_client, deployed_artifact):
        repo, _ = deployed_artifact
        result = integration_client.search_items_by_properties(
            {"test.source": "integration"},
            repos=repo,
            x_result_detail="info",
        )
        assert isinstance(result, SearchItemsByPropertiesResponse)
