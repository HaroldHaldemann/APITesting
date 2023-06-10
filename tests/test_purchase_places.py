import server
from server import app
from tests import mocks


class TestPurchasePlaces:

    client = app.test_client()

    def setup_method(self):
        server.CLUBS = mocks.MOCK_CLUBS
        server.COMPETITIONS = mocks.MOCK_COMPETITIONS
    
    def test_valid_required_places(self):
        # given
        club_name = mocks.MOCK_CLUBS[0]['name']
        competition_name = mocks.MOCK_COMPETITIONS[0]['name']

        # when
        result = self.client.post(
            "/purchase-places",
            data={
                "places": 3,
                "club": club_name,
                "competition": competition_name
            }
        )

        # then
        assert result.status_code == 200
        assert "Great-booking complete!" in result.data.decode()
    
    def test_invalid_required_places(self):
        # given
        club_name = mocks.MOCK_CLUBS[0]['name']
        competition_name = mocks.MOCK_COMPETITIONS[0]['name']

        # when
        result = self.client.post(
            "/purchase-places",
            data={
                "places": "NaN",
                "club": club_name,
                "competition": competition_name
            }
        )

        # then
        assert result.status_code == 400
        assert "Please enter a valid number (between 1 and 12)." in result.data.decode()
    
    def test_invalid_required_places_number(self):
        # given
        club_name = mocks.MOCK_CLUBS[0]['name']
        competition_name = mocks.MOCK_COMPETITIONS[0]['name']

        # when
        result = self.client.post(
            "/purchase-places",
            data={
                "places": 15,
                "club": club_name,
                "competition": competition_name
            }
        )

        # then
        assert result.status_code == 400
        assert "Please enter a valid number (between 1 and 12)." in result.data.decode()
    
    def test_reach_max_places_in_competition(self):
        # given
        club_name = mocks.MOCK_CLUBS[0]['name']
        competition_name = mocks.MOCK_COMPETITIONS[0]['name']

        # when
        self.client.post(
            "/purchase-places",
            data={
                "places": 7,
                "club": club_name,
                "competition": competition_name
            }
        )
        result =self.client.post(
            "/purchase-places",
            data={
                "places": 7,
                "club": club_name,
                "competition": competition_name
            }
        )

        # then
        assert result.status_code == 400
        assert "You cannot book more than 12 places in a competition." in result.data.decode()
    
    def test_not_enough_competition_places(self):
        # given
        club_name = mocks.MOCK_CLUBS[0]['name']
        competition = mocks.MOCK_COMPETITIONS[1]

        # when
        result = self.client.post(
            "/purchase-places",
            data={
                "places": 7,
                "club": club_name,
                "competition": competition['name']
            }
        )

        # then
        assert result.status_code == 400
        assert f"There are only {competition['numberOfPlaces']} places available." in result.data.decode()
    
    def test_not_enough_points(self):
        # given
        club = mocks.MOCK_CLUBS[1]
        competition_name = mocks.MOCK_COMPETITIONS[0]['name']
        places = 3

        # when
        result = self.client.post(
            "/purchase-places",
            data={
                "places": places,
                "club": club['name'],
                "competition": competition_name
            }
        )

        # then
        assert result.status_code == 400
        assert f"You do not have enough points: {places * 3 - int(club['points'])} points missing." in result.data.decode()