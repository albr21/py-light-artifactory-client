from light_artifactory_client.exceptions import HTTPError, NotFoundError

class TestExceptionNotFoundError:
    def test_exception_not_found_status_code(self):
        assert NotFoundError().status_code == 404

    def test_exception_not_found_inherits_http_error(self):
        assert isinstance(NotFoundError(), HTTPError)

    def test_exception_not_found_custom_message(self):
        assert NotFoundError("Not Found").body == "Not Found"
