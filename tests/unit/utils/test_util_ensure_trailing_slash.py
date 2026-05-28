from light_artifactory_client.utils import ensure_trailing_slash

class TestUtilEnsureTrailingSlash:
    def test_util_ensure_trailing_slash_adds_slash(self):
        assert ensure_trailing_slash("https://example.com") == "https://example.com/"

    def test_util_ensure_trailing_slash_no_double_slash(self):
        assert ensure_trailing_slash("https://example.com/") == "https://example.com/"

    def test_util_ensure_trailing_slash_empty_string(self):
        assert ensure_trailing_slash("") == "/"
