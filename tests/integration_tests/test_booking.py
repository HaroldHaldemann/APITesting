import server
from server import app

from tests import mocks


class TestBooking:
    client = app.test_client()

    def setup_method(self):
        server.CLUBS = mocks.MOCK_CLUBS
        server.COMPETITIONS = mocks.MOCK_COMPETITIONS
        server.PAST_COMPETITIONS = mocks.MOCK_PAST_COMPETITIONS
        server.PRESENT_COMPETITIONS = mocks.MOCK_PRESENT_COMPETITIONS
    
    def test_valid_booking_with_valid_club_and_competition(self):
        # given
        club = mocks.MOCK_CLUBS[0]
        competition = mocks.MOCK_COMPETITIONS[0]
        required_places = 5
        club_points = int(club['points'])


        # when
        self.client.post(
            "/purchase-places",
            data = {
                "club": club['name'],
                "competition": competition['name'],
                "places": required_places
            }
        )
        result = self.client.get("/club-points")

        # then
        assert result.status_code == 200
        assert f"<td>{club['name']}</td>\n            <td>{club_points - required_places * 3}</td>" in result.data.decode()
    
    def test_booking_with_valid_club_and_competition_invalid_required_places(self):
        # given
        club = mocks.MOCK_CLUBS[0]
        competition = mocks.MOCK_COMPETITIONS[0]
        required_places = 15
        club_points = int(club['points'])


        # when
        self.client.post(
            "/purchase-places",
            data = {
                "club": club['name'],
                "competition": competition['name'],
                "places": required_places
            }
        )
        result = self.client.get("/club-points")

        # then
        assert result.status_code == 200
        assert f"<td>{club['name']}</td>\n            <td>{club_points}</td>" in result.data.decode()

    def test_booking_with_valid_club_and_competition_invalid_too_many_places_for_competition(self):
        # given
        club = mocks.MOCK_CLUBS[0]
        competition = mocks.MOCK_COMPETITIONS[0]
        required_places = 10
        club_points = int(club['points'])


        # when
        self.client.post(
            "/purchase-places",
            data = {
                "club": club['name'],
                "competition": competition['name'],
                "places": required_places
            }
        )
        result = self.client.get("/club-points")

        # then
        assert result.status_code == 200
        assert f"<td>{club['name']}</td>\n            <td>{club_points}</td>" in result.data.decode()