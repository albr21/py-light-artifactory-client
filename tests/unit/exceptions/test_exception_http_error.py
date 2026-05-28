from light_artifactory_client.exceptions import HTTPError, LightArtifactoryClientError

class TestExceptionHTTPError:
    def test_exception_http_error_attributes(self):
        exc = HTTPError(500, "Internal Server Error")
        assert exc.status_code == 500
        assert exc.body == "Internal Server Error"
        assert "500" in str(exc)
        assert "Internal Server Error" in str(exc)

    def test_exception_http_error_inherits_base(self):
        assert isinstance(HTTPError(500, "err"), LightArtifactoryClientError)
