from light_artifactory_client.utils import to_query_properties

class TestUtilToQueryProperties:
    def test_util_to_query_properties_none(self):
        assert to_query_properties(None) == ""

    def test_util_to_query_properties_empty_dict(self):
        assert to_query_properties({}) == ""

    def test_util_to_query_properties_single(self):
        assert to_query_properties({"key": "value"}) == "?key=value"

    def test_util_to_query_properties_multiple(self):
        assert to_query_properties({"a": "1", "b": "2"}) == "?a=1&b=2"

    def test_util_to_query_properties_encodes_special_chars(self):
        result = to_query_properties({"key space": "val&ue"})
        assert "key%20space" in result
        assert "val%26ue" in result
