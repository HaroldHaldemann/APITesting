import server
from server import app

from tests import mocks


class TestBooking:
    client = app.test_client()

    def setup_method(self):
        server.CLUBS = mocks.MOCK_CLUBS
    
    def test_login_valid_email(self):
        # given
        club = mocks.MOCK_CLUBS[0]
        email = club['email']

        # when
        result = self.client.post(
            "/show-summary",
            data = {"email": email}
        )

        # then
        assert result.status_code == 200
        assert f"<h2>Welcome, {email}</h2>" in result.data.decode()