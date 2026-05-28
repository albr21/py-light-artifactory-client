import json

from light_artifactory_client.responses import Response

class TestResponseBase:
    def test_response_status_code(self):
        assert Response(status_code=200, body="OK").status_code == 200

    def test_response_body(self):
        assert Response(status_code=200, body="hello").body == "hello"

    def test_response_headers(self):
        resp = Response(status_code=200, body="", headers={"X-Custom": "val"})
        assert resp.headers == {"X-Custom": "val"}

    def test_response_default_headers(self):
        assert Response(status_code=200, body="").headers == {}

    def test_response_json(self):
        body = json.dumps({"key": "value"})
        assert Response(status_code=200, body=body).json() == {"key": "value"}
