import pytest

from light_artifactory_client.responses import SearchAQLResponse

pytestmark = pytest.mark.integration

class TestIntegrationSearchAQL:
    def test_integration_search_aql_success(self, integration_client, deployed_artifact):
        repo, _ = deployed_artifact
        query = f'items.find({{"repo":"{repo}"}})'  
        result = integration_client.search_aql(query)
        assert isinstance(result, SearchAQLResponse)
        assert isinstance(result.results, list)

    def test_integration_search_aql_empty_results(self, integration_client):
        result = integration_client.search_aql('items.find({"repo":"nonexistent-repo-xyz-abc"})')
        assert isinstance(result, SearchAQLResponse)
        assert result.results == []
