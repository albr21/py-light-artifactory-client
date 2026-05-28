import pytest

from unittest.mock import MagicMock

from light_artifactory_client import ForbiddenError, NotFoundError
from light_artifactory_client.exceptions import InvalidArgumentError
from light_artifactory_client.responses import DeleteItemResponse

from .conftest import mock_response
from .conftest import SERVER_URL

class TestOperationDeleteItem:
    def test_operation_delete_item_success(self, client):
        client.session.delete = MagicMock(return_value=mock_response(204, ""))

        result = client.delete_item("repo", "org/artifact.jar")

        assert isinstance(result, DeleteItemResponse)
        assert result.status_code == 204

    def test_operation_delete_item_empty_repo_raises(self, client):
        with pytest.raises(InvalidArgumentError):
            client.delete_item("", "path")

    def test_operation_delete_item_empty_path_raises(self, client):
        with pytest.raises(InvalidArgumentError):
            client.delete_item("repo", "")

    def test_operation_delete_item_url_construction(self, client):
        client.session.delete = MagicMock(return_value=mock_response(204, ""))
        client.delete_item("libs-release", "com/example/old.jar")
        called_url = client.session.delete.call_args[0][0]
        assert called_url == f"{SERVER_URL}artifactory/libs-release/com/example/old.jar"

    def test_operation_delete_item_404_raises(self, client):
        client.session.delete = MagicMock(return_value=mock_response(404))
        with pytest.raises(NotFoundError):
            client.delete_item("repo", "path")

    def test_operation_delete_item_403_raises(self, client):
        client.session.delete = MagicMock(return_value=mock_response(403))
        with pytest.raises(ForbiddenError):
            client.delete_item("repo", "path")
