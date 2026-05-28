from light_artifactory_client.exceptions import LightArtifactoryClientError

class TestExceptionBase:
    def test_exception_base_error_message(self):
        exc = LightArtifactoryClientError("something went wrong")
        assert "something went wrong" in str(exc)
        assert isinstance(exc, Exception)
