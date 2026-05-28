import json
import pytest

from unittest.mock import MagicMock

from light_artifactory_client import NotAuthenticatedError
from light_artifactory_client.responses import SearchAQLResponse

from .conftest import mock_response
from .conftest import SERVER_URL

class TestOperationSearchAQL:
    def test_operation_search_aql_success(self, client):
        body = json.dumps({"results": [{"name": "artifact.jar", "repo": "libs"}]})
        client.session.post = MagicMock(return_value=mock_response(200, body))

        result = client.search_aql('items.find({"repo":"libs"})')

        assert isinstance(result, SearchAQLResponse)
        assert len(result.results) == 1
        assert result.results[0]["name"] == "artifact.jar"

    def test_operation_search_aql_url_construction(self, client):
        client.session.post = MagicMock(return_value=mock_response(200, '{"results": []}'))
        client.search_aql("items.find()")
        called_url = client.session.post.call_args[0][0]
        assert called_url == f"{SERVER_URL}artifactory/api/search/aql"

    def test_operation_search_aql_content_type_header(self, client):
        client.session.post = MagicMock(return_value=mock_response(200, '{"results": []}'))
        client.search_aql("items.find()")
        headers = client.session.post.call_args[1]["headers"]
        assert headers["Content-Type"] == "text/plain"
        assert headers["Accept"] == "application/json"

    def test_operation_search_aql_query_sent_as_body(self, client):
        client.session.post = MagicMock(return_value=mock_response(200, '{"results": []}'))
        query = 'items.find({"repo":"libs-release"})'
        client.search_aql(query)
        assert client.session.post.call_args[1]["data"] == query

    def test_operation_search_aql_401_raises(self, client):
        client.session.post = MagicMock(return_value=mock_response(401))
        with pytest.raises(NotAuthenticatedError):
            client.search_aql("items.find()")
