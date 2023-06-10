import server
from server import app
from tests import mocks

class TestClubPoints:
    client = app.test_client()

    client = app.test_client()

    def setup_method(self):
        server.CLUBS = mocks.MOCK_CLUBS
        server.COMPETITIONS = mocks.MOCK_COMPETITIONS

    def test_club_points(self):
        result = self.client.get("/club-points")
        assert result.status_code == 200
