import json

from light_artifactory_client.responses import SearchAQLResponse

class TestResponseSearchAQL:
    def test_response_search_aql_results(self):
        body = json.dumps({"results": [{"name": "artifact.jar"}]})
        resp = SearchAQLResponse(status_code=200, body=body)
        assert len(resp.results) == 1
        assert resp.results[0]["name"] == "artifact.jar"

    def test_response_search_aql_empty(self):
        assert SearchAQLResponse(status_code=200, body='{"results": []}').results == []
