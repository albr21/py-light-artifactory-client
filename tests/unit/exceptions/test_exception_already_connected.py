from light_artifactory_client.exceptions import AlreadyConnectedError, LightArtifactoryClientError

class TestExceptionAlreadyConnectedError:
    def test_exception_already_connected_message(self):
        assert "Already connected" in str(AlreadyConnectedError())

    def test_exception_already_connected_inherits_base(self):
        assert isinstance(AlreadyConnectedError(), LightArtifactoryClientError)
