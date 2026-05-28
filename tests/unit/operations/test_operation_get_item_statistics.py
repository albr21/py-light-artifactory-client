import json
import pytest

from unittest.mock import MagicMock

from light_artifactory_client.exceptions import InvalidArgumentError
from light_artifactory_client.responses import GetItemStatisticsResponse

from .conftest import mock_response

class TestOperationGetItemStatistics:
    def test_operation_get_item_statistics_success(self, client):
        body = json.dumps({"downloadCount": 42, "lastDownloaded": 1234567890})
        client.session.get = MagicMock(return_value=mock_response(200, body))

        result = client.get_item_statistics("repo", "path/file.jar")

        assert isinstance(result, GetItemStatisticsResponse)
        assert result.json()["downloadCount"] == 42

    def test_operation_get_item_statistics_empty_repo_raises(self, client):
        with pytest.raises(InvalidArgumentError):
            client.get_item_statistics("", "path")

    def test_operation_get_item_statistics_empty_path_raises(self, client):
        with pytest.raises(InvalidArgumentError):
            client.get_item_statistics("repo", "")

    def test_operation_get_item_statistics_url_ends_with_stats_param(self, client):
        client.session.get = MagicMock(return_value=mock_response(200, "{}"))
        client.get_item_statistics("repo", "path.jar")
        called_url = client.session.get.call_args[0][0]
        assert called_url.endswith("?stats")
