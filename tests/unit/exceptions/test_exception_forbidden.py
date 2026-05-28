from light_artifactory_client.exceptions import ForbiddenError, HTTPError

class TestExceptionForbiddenError:
    def test_exception_forbidden_status_code(self):
        assert ForbiddenError().status_code == 403

    def test_exception_forbidden_inherits_http_error(self):
        assert isinstance(ForbiddenError(), HTTPError)

    def test_exception_forbidden_custom_message(self):
        assert ForbiddenError("Forbidden").body == "Forbidden"
