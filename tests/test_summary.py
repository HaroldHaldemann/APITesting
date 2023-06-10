from tests import mocks
from server import app


class TestShowSummary:

    client = app.test_client()

    def test_valid_email(self):
        # given
        email = mocks.MOCK_CLUBS[0]["email"]

        # when
        result = self.client.post("/show-summary", data={"email": email})

        # then
        assert result.status_code == 200

    def test_invalid_email(self):
        # given
        email = "invalid_email"

        # when
        result = self.client.post("/show-summary", data={"email": email})

        # then
        assert result.status_code == 404
        assert f"No account related to this email: {email}." in result.data.decode('utf-8')

    def test_empty_email(self):
        # given
        email = ""

        # when
        result = self.client.post("/show-summary", data={"email": email})

        # then
        assert result.status_code == 400
        assert "Please enter your email." in result.data.decode('utf-8')