from light_artifactory_client.utils import to_matrix_properties

class TestUtilToMatrixProperties:
    def test_util_to_matrix_properties_none(self):
        assert to_matrix_properties(None) == ""

    def test_util_to_matrix_properties_empty_dict(self):
        assert to_matrix_properties({}) == ""

    def test_util_to_matrix_properties_single(self):
        assert to_matrix_properties({"key": "value"}) == ";key=value"

    def test_util_to_matrix_properties_multiple(self):
        assert to_matrix_properties({"a": "1", "b": "2"}) == ";a=1;b=2"

    def test_util_to_matrix_properties_list_value(self):
        assert to_matrix_properties({"key": ["v1", "v2"]}) == ";key=v1;key=v2"

    def test_util_to_matrix_properties_encodes_special_chars(self):
        result = to_matrix_properties({"key with space": "val/ue"})
        assert "key%20with%20space" in result
        assert "val%2Fue" in result

    def test_util_to_matrix_properties_mixed_values(self):
        result = to_matrix_properties({"single": "val", "multi": ["a", "b"]})
        assert ";single=val" in result
        assert ";multi=a" in result
        assert ";multi=b" in result
