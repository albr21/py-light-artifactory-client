from light_artifactory_client.exceptions import HTTPError, NotAuthenticatedError

class TestExceptionNotAuthenticatedError:
    def test_exception_not_authenticated_status_code(self):
        assert NotAuthenticatedError().status_code == 401

    def test_exception_not_authenticated_inherits_http_error(self):
        assert isinstance(NotAuthenticatedError(), HTTPError)

    def test_exception_not_authenticated_custom_message(self):
        assert NotAuthenticatedError("Unauthorized").body == "Unauthorized"
