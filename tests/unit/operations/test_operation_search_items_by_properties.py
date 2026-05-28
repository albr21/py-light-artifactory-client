import json
import pytest

from unittest.mock import MagicMock

from light_artifactory_client import ForbiddenError, NotAuthenticatedError
from light_artifactory_client.exceptions import InvalidArgumentError
from light_artifactory_client.responses import SearchItemsByPropertiesResponse

from .conftest import mock_response
from .conftest import SERVER_URL

class TestOperationSearchItemsByProperties:
    def test_operation_search_by_props_success(self, client):
        body = json.dumps({"results": [{"uri": "http://example.com/item"}]})
        client.session.get = MagicMock(return_value=mock_response(200, body))

        result = client.search_items_by_properties({"build.name": "my-build"})

        assert isinstance(result, SearchItemsByPropertiesResponse)
        assert len(result.results) == 1

    def test_operation_search_by_props_none_raises(self, client):
        with pytest.raises(InvalidArgumentError, match="properties must be a dict"):
            client.search_items_by_properties(None)

    def test_operation_search_by_props_invalid_x_result_detail_raises(self, client):
        with pytest.raises(InvalidArgumentError, match="x_result_detail must be one of"):
            client.search_items_by_properties({"key": "val"}, x_result_detail="invalid")

    def test_operation_search_by_props_x_result_detail_info_header(self, client):
        client.session.get = MagicMock(return_value=mock_response(200, '{"results": []}'))
        client.search_items_by_properties({"key": "val"}, x_result_detail="info")
        assert client.session.get.call_args[1]["headers"]["X-Result-Detail"] == "info"

    def test_operation_search_by_props_x_result_detail_properties_header(self, client):
        client.session.get = MagicMock(return_value=mock_response(200, '{"results": []}'))
        client.search_items_by_properties({"key": "val"}, x_result_detail="properties")
        assert client.session.get.call_args[1]["headers"]["X-Result-Detail"] == "properties"

    def test_operation_search_by_props_x_result_detail_both_header(self, client):
        client.session.get = MagicMock(return_value=mock_response(200, '{"results": []}'))
        client.search_items_by_properties({"key": "val"}, x_result_detail="info, properties")
        assert client.session.get.call_args[1]["headers"]["X-Result-Detail"] == "info, properties"

    def test_operation_search_by_props_repos_in_url(self, client):
        client.session.get = MagicMock(return_value=mock_response(200, '{"results": []}'))
        client.search_items_by_properties({"key": "val"}, repos="my-repo")
        called_url = client.session.get.call_args[0][0]
        assert "repos=my-repo" in called_url

    def test_operation_search_by_props_url_construction(self, client):
        client.session.get = MagicMock(return_value=mock_response(200, '{"results": []}'))
        client.search_items_by_properties({"build.name": "my-build"})
        called_url = client.session.get.call_args[0][0]
        assert f"{SERVER_URL}artifactory/api/search/prop?" in called_url

    def test_operation_search_by_props_does_not_mutate_input(self, client):
        client.session.get = MagicMock(return_value=mock_response(200, '{"results": []}'))
        props = {"key": "val"}
        client.search_items_by_properties(props, repos="my-repo")
        assert "repos" not in props

    def test_operation_search_by_props_401_raises(self, client):
        client.session.get = MagicMock(return_value=mock_response(401))
        with pytest.raises(NotAuthenticatedError):
            client.search_items_by_properties({"key": "val"})

    def test_operation_search_by_props_403_raises(self, client):
        client.session.get = MagicMock(return_value=mock_response(403))
        with pytest.raises(ForbiddenError):
            client.search_items_by_properties({"key": "val"})
