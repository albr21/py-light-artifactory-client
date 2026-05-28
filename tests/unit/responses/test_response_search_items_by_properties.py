import json

from light_artifactory_client.responses import SearchItemsByPropertiesResponse

class TestResponseSearchItemsByProperties:
    def test_response_search_by_props_results(self):
        body = json.dumps({"results": [{"uri": "http://example.com/item"}]})
        resp = SearchItemsByPropertiesResponse(status_code=200, body=body)
        assert len(resp.results) == 1

    def test_response_search_by_props_empty(self):
        assert SearchItemsByPropertiesResponse(status_code=200, body='{"results": []}').results == []
