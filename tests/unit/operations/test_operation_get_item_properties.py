import json
import pytest

from unittest.mock import MagicMock

from light_artifactory_client import NotAuthenticatedError
from light_artifactory_client.exceptions import InvalidArgumentError
from light_artifactory_client.responses import GetItemPropertiesResponse

from .conftest import mock_response

class TestOperationGetItemProperties:
    def test_operation_get_item_properties_success(self, client):
        body = json.dumps({"properties": {"build.name": ["my-build"]}})
        client.session.get = MagicMock(return_value=mock_response(200, body))

        result = client.get_item_properties("repo", "path/file.jar")

        assert isinstance(result, GetItemPropertiesResponse)
        assert "build.name" in result.json()["properties"]

    def test_operation_get_item_properties_empty_repo_raises(self, client):
        with pytest.raises(InvalidArgumentError):
            client.get_item_properties("", "path")

    def test_operation_get_item_properties_none_path_raises(self, client):
        with pytest.raises(InvalidArgumentError):
            client.get_item_properties("repo", None)

    def test_operation_get_item_properties_url_ends_with_properties_param(self, client):
        client.session.get = MagicMock(return_value=mock_response(200, "{}"))
        client.get_item_properties("repo", "path.jar")
        called_url = client.session.get.call_args[0][0]
        assert called_url.endswith("?properties")

    def test_operation_get_item_properties_401_raises(self, client):
        client.session.get = MagicMock(return_value=mock_response(401))
        with pytest.raises(NotAuthenticatedError):
            client.get_item_properties("repo", "path")
