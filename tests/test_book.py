import server
from server import app
from tests import mocks


class TestBook:

    client = app.test_client()

    def setup_method(self):
        server.CLUBS = mocks.MOCK_CLUBS
        server.COMPETITIONS = mocks.MOCK_COMPETITIONS
        server.PAST_COMPETITIONS = mocks.MOCK_PAST_COMPETITIONS
        server.PRESENT_COMPETITIONS = mocks.MOCK_PRESENT_COMPETITIONS

    def test_book_competition(self):
        # given
        club_name = mocks.MOCK_CLUBS[0]['name']
        competition_name = mocks.MOCK_COMPETITIONS[0]['name']

        # when
        result = self.client.get(f"/book/{competition_name}/{club_name}")

        # then
        assert result.status_code == 200

    def test_book_non_existant_competition(self):
        # given
        club_name = mocks.MOCK_CLUBS[0]['name']
        competition_name = "invalid_competition_name"

        # when
        result = self.client.get(f"/book/{competition_name}/{club_name}")

        # then
        assert result.status_code == 404
        assert f"There is no competition with the name {competition_name}." in result.data.decode()
    
    def test_book_closed_competition(self):
        # given
        club_name = mocks.MOCK_CLUBS[0]['name']
        competition_name = mocks.MOCK_COMPETITIONS[2]['name']

        # when
        result = self.client.get(f"/book/{competition_name}/{club_name}")

        # then
        assert result.status_code == 400
        assert f"The competition {competition_name} is over." in result.data.decode()
    
    def test_book_with_non_existant_club(self):
        # given
        club_name = "invalid_club_name"
        competition_name = mocks.MOCK_COMPETITIONS[0]['name']

        # when
        result = self.client.get(f"/book/{competition_name}/{club_name}")

        # then
        assert result.status_code == 404
        assert f"There is no club with the name {club_name}." in result.data.decode()
