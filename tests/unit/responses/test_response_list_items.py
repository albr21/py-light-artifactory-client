import json

from light_artifactory_client.responses import ListItemsResponse

class TestResponseListItems:
    def test_response_list_items_items(self):
        body = json.dumps({"files": [{"uri": "/file1.txt"}, {"uri": "/file2.txt"}]})
        resp = ListItemsResponse(status_code=200, body=body)
        assert len(resp.items) == 2
        assert resp.items[0]["uri"] == "/file1.txt"

    def test_response_list_items_empty(self):
        assert ListItemsResponse(status_code=200, body='{"files": []}').items == []

    def test_response_list_items_missing_key(self):
        assert ListItemsResponse(status_code=200, body="{}").items == []
