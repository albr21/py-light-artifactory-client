from light_artifactory_client.exceptions import InvalidArgumentError, LightArtifactoryClientError

class TestExceptionInvalidArgumentError:
    def test_exception_invalid_argument_message(self):
        assert "bad argument" in str(InvalidArgumentError("bad argument"))

    def test_exception_invalid_argument_inherits_base(self):
        assert isinstance(InvalidArgumentError("bad"), LightArtifactoryClientError)
