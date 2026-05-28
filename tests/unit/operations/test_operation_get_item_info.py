import json
import pytest

from unittest.mock import MagicMock

from light_artifactory_client import ForbiddenError, HTTPError, NotAuthenticatedError, NotFoundError
from light_artifactory_client.exceptions import InvalidArgumentError
from light_artifactory_client.responses import GetItemInfoResponse

from .conftest import mock_response
from .conftest import SERVER_URL

class TestOperationGetItemInfo:
    def test_operation_get_item_info_success(self, client):
        body = json.dumps({"repo": "libs-release", "path": "/com/example"})
        client.session.get = MagicMock(return_value=mock_response(200, body))

        result = client.get_item_info("libs-release", "com/example/artifact.jar")

        assert isinstance(result, GetItemInfoResponse)
        assert result.status_code == 200
        assert result.json()["repo"] == "libs-release"
        client.session.get.assert_called_once()

    def test_operation_get_item_info_empty_repo_raises(self, client):
        with pytest.raises(InvalidArgumentError):
            client.get_item_info("", "some/path")

    def test_operation_get_item_info_none_path_raises(self, client):
        with pytest.raises(InvalidArgumentError):
            client.get_item_info("repo", None)

    def test_operation_get_item_info_url_construction(self, client):
        client.session.get = MagicMock(return_value=mock_response(200, "{}"))
        client.get_item_info("my-repo", "org/artifact.jar")
        called_url = client.session.get.call_args[0][0]
        assert called_url == f"{SERVER_URL}artifactory/api/storage/my-repo/org/artifact.jar"

    def test_operation_get_item_info_401_raises(self, client):
        client.session.get = MagicMock(return_value=mock_response(401))
        with pytest.raises(NotAuthenticatedError):
            client.get_item_info("repo", "path")

    def test_operation_get_item_info_403_raises(self, client):
        client.session.get = MagicMock(return_value=mock_response(403))
        with pytest.raises(ForbiddenError):
            client.get_item_info("repo", "path")

    def test_operation_get_item_info_404_raises(self, client):
        client.session.get = MagicMock(return_value=mock_response(404))
        with pytest.raises(NotFoundError):
            client.get_item_info("repo", "path")

    def test_operation_get_item_info_500_raises(self, client):
        client.session.get = MagicMock(return_value=mock_response(500))
        with pytest.raises(HTTPError):
            client.get_item_info("repo", "path")
