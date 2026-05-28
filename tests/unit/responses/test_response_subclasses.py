from light_artifactory_client.responses import (
    DeleteItemResponse,
    DeployArtifactResponse,
    GetItemInfoResponse,
    GetItemPropertiesResponse,
    GetItemStatisticsResponse,
    ListItemsResponse,
    Response,
    RetrieveArtifactResponse,
    RetrieveArtifactUsingUriResponse,
    SearchAQLResponse,
    SearchItemsByPropertiesResponse,
)

class TestResponseSubclasses:
    def test_response_subclass_get_item_info(self):
        assert isinstance(GetItemInfoResponse(status_code=200, body="{}"), Response)

    def test_response_subclass_get_item_properties(self):
        assert isinstance(GetItemPropertiesResponse(status_code=200, body="{}"), Response)

    def test_response_subclass_get_item_statistics(self):
        assert isinstance(GetItemStatisticsResponse(status_code=200, body="{}"), Response)

    def test_response_subclass_deploy_artifact(self):
        assert isinstance(DeployArtifactResponse(status_code=201, body="{}"), Response)

    def test_response_subclass_retrieve_artifact(self):
        assert isinstance(RetrieveArtifactResponse(status_code=200, body="data"), Response)

    def test_response_subclass_retrieve_artifact_using_uri(self):
        assert isinstance(RetrieveArtifactUsingUriResponse(status_code=200, body="data"), Response)

    def test_response_subclass_delete_item(self):
        assert isinstance(DeleteItemResponse(status_code=204, body=""), Response)

    def test_response_subclass_list_items(self):
        assert isinstance(ListItemsResponse(status_code=200, body='{"files":[]}'), Response)

    def test_response_subclass_search_aql(self):
        assert isinstance(SearchAQLResponse(status_code=200, body='{"results":[]}'), Response)

    def test_response_subclass_search_items_by_properties(self):
        assert isinstance(SearchItemsByPropertiesResponse(status_code=200, body='{"results":[]}'), Response)
