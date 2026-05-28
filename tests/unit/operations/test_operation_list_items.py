import json
import pytest

from unittest.mock import MagicMock

from light_artifactory_client import NotFoundError
from light_artifactory_client.exceptions import InvalidArgumentError
from light_artifactory_client.responses import ListItemsResponse

from .conftest import mock_response

class TestOperationListItems:
    def test_operation_list_items_success(self, client):
        body = json.dumps({"files": [{"uri": "/file1.txt", "size": 100}]})
        client.session.get = MagicMock(return_value=mock_response(200, body))

        result = client.list_items("repo")

        assert isinstance(result, ListItemsResponse)
        assert len(result.items) == 1
        assert result.items[0]["uri"] == "/file1.txt"

    def test_operation_list_items_empty_repo_raises(self, client):
        with pytest.raises(InvalidArgumentError):
            client.list_items("")

    def test_operation_list_items_invalid_deep_raises(self, client):
        with pytest.raises(InvalidArgumentError, match="deep must be a boolean"):
            client.list_items("repo", deep="yes")

    def test_operation_list_items_negative_depth_raises(self, client):
        with pytest.raises(InvalidArgumentError, match="depth must be None or a positive integer"):
            client.list_items("repo", depth=-1)

    def test_operation_list_items_zero_depth_raises(self, client):
        with pytest.raises(InvalidArgumentError, match="depth must be None or a positive integer"):
            client.list_items("repo", depth=0)

    def test_operation_list_items_invalid_list_folders_raises(self, client):
        with pytest.raises(InvalidArgumentError, match="list_folders must be a boolean"):
            client.list_items("repo", list_folders="yes")

    def test_operation_list_items_invalid_include_root_raises(self, client):
        with pytest.raises(InvalidArgumentError, match="include_root must be a boolean"):
            client.list_items("repo", include_root="yes")

    def test_operation_list_items_deep_url(self, client):
        client.session.get = MagicMock(return_value=mock_response(200, '{"files": []}'))
        client.list_items("repo", deep=True)
        called_url = client.session.get.call_args[0][0]
        assert "deep=1" in called_url

    def test_operation_list_items_depth_in_url(self, client):
        client.session.get = MagicMock(return_value=mock_response(200, '{"files": []}'))
        client.list_items("repo", depth=3)
        called_url = client.session.get.call_args[0][0]
        assert "depth=3" in called_url

    def test_operation_list_items_default_params_in_url(self, client):
        client.session.get = MagicMock(return_value=mock_response(200, '{"files": []}'))
        client.list_items("repo")
        called_url = client.session.get.call_args[0][0]
        assert "deep=0" in called_url
        assert "listFolders=0" in called_url
        assert "includeRoot=0" in called_url

    def test_operation_list_items_404_raises(self, client):
        client.session.get = MagicMock(return_value=mock_response(404))
        with pytest.raises(NotFoundError):
            client.list_items("repo")
