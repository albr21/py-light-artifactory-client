import pytest

from unittest.mock import MagicMock

from light_artifactory_client import HTTPError

from .conftest import mock_response

class TestOperationHandleResponse:
    def test_operation_handle_response_unexpected_2xx_raises(self, client):
        client.session.put = MagicMock(return_value=mock_response(200, "OK"))
        with pytest.raises(HTTPError):
            client.deploy_artifact("repo", "path", b"content")

    def test_operation_handle_response_status_code_in_exception(self, client):
        client.session.get = MagicMock(return_value=mock_response(503, "Service Unavailable"))
        with pytest.raises(HTTPError) as exc_info:
            client.get_item_info("repo", "path")
        assert exc_info.value.status_code == 503
        assert "Service Unavailable" in exc_info.value.body
