import pytest

from unittest.mock import MagicMock

from light_artifactory_client import NotAuthenticatedError
from light_artifactory_client.exceptions import InvalidArgumentError
from light_artifactory_client.responses import RetrieveArtifactUsingUriResponse

from .conftest import mock_response

class TestOperationRetrieveArtifactUsingUri:
    def test_operation_retrieve_using_uri_success(self, client):
        uri = "https://example.com/artifactory/repo/file.jar"
        client.session.get = MagicMock(return_value=mock_response(200, "data"))

        result = client.retrieve_artifact_using_uri(uri)

        assert isinstance(result, RetrieveArtifactUsingUriResponse)
        assert result.body == "data"

    def test_operation_retrieve_using_uri_empty_raises(self, client):
        with pytest.raises(InvalidArgumentError, match="uri is required"):
            client.retrieve_artifact_using_uri("")

    def test_operation_retrieve_using_uri_none_raises(self, client):
        with pytest.raises(InvalidArgumentError, match="uri is required"):
            client.retrieve_artifact_using_uri(None)

    def test_operation_retrieve_using_uri_non_string_raises(self, client):
        with pytest.raises(InvalidArgumentError, match="uri must be a string"):
            client.retrieve_artifact_using_uri(12345)

    def test_operation_retrieve_using_uri_ftp_scheme_raises(self, client):
        with pytest.raises(InvalidArgumentError, match="uri must start with"):
            client.retrieve_artifact_using_uri("ftp://example.com/artifactory/repo/file.jar")

    def test_operation_retrieve_using_uri_no_artifactory_raises(self, client):
        with pytest.raises(InvalidArgumentError, match="uri must contain 'artifactory'"):
            client.retrieve_artifact_using_uri("https://example.com/repo/file.jar")

    def test_operation_retrieve_using_uri_http_accepted(self, client):
        uri = "http://example.com/artifactory/repo/file.jar"
        client.session.get = MagicMock(return_value=mock_response(200, "data"))
        result = client.retrieve_artifact_using_uri(uri)
        assert isinstance(result, RetrieveArtifactUsingUriResponse)

    def test_operation_retrieve_using_uri_401_raises(self, client):
        uri = "https://example.com/artifactory/repo/file.jar"
        client.session.get = MagicMock(return_value=mock_response(401))
        with pytest.raises(NotAuthenticatedError):
            client.retrieve_artifact_using_uri(uri)
