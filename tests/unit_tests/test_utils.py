from tests import mocks
import utils

class TestUtils:

    def test_initialize_booked_places(self):
        # given
        clubs = mocks.MOCK_CLUBS
        competitions = mocks.MOCK_COMPETITIONS

        # when
        result = utils.initialize_booked_places(competitions, clubs)

        # then
        assert result == {
            'Push&Pull': {'Simply Lift': 0, 'Iron Temple': 0, 'She Lifts': 0},
            'MrHuman': {'Simply Lift': 0, 'Iron Temple': 0, 'She Lifts': 0},
            'Spring Festival': {'Simply Lift': 0, 'Iron Temple': 0, 'She Lifts': 0},
            'Fall Classic': {'Simply Lift': 0, 'Iron Temple': 0, 'She Lifts': 0}
        }

    def test_check_club_places_valid(self):
        # given
        club_name = mocks.MOCK_CLUBS[0]['name']
        competition_name = mocks.MOCK_COMPETITIONS[0]['name']
        booked_places = {
            'Push&Pull': {'Simply Lift': 0, 'Iron Temple': 0, 'She Lifts': 0},
            'MrHuman': {'Simply Lift': 0, 'Iron Temple': 0, 'She Lifts': 0},
            'Spring Festival': {'Simply Lift': 0, 'Iron Temple': 0, 'She Lifts': 0},
            'Fall Classic': {'Simply Lift': 0, 'Iron Temple': 0, 'She Lifts': 0}
        }
        required_places = 7

        # when
        result = utils.check_club_places(competition_name, club_name, booked_places, required_places)

        # then
        assert result == True
    
    def test_check_club_places_invalid(self):
        # given
        club_name = mocks.MOCK_CLUBS[0]['name']
        competition_name = mocks.MOCK_COMPETITIONS[0]['name']
        booked_places = {
            'Push&Pull': {'Simply Lift': 9, 'Iron Temple': 0, 'She Lifts': 0},
            'MrHuman': {'Simply Lift': 0, 'Iron Temple': 0, 'She Lifts': 0},
            'Spring Festival': {'Simply Lift': 0, 'Iron Temple': 0, 'She Lifts': 0},
            'Fall Classic': {'Simply Lift': 0, 'Iron Temple': 0, 'She Lifts': 0}
        }
        required_places = 7

        # when
        result = utils.check_club_places(competition_name, club_name, booked_places, required_places)

        # then
        assert result == False
    
    def test_update_booked_places(self):
        # given
        club_name = mocks.MOCK_CLUBS[0]['name']
        competition_name = mocks.MOCK_COMPETITIONS[0]['name']
        booked_places = {
            'Push&Pull': {'Simply Lift': 0, 'Iron Temple': 0, 'She Lifts': 0},
            'MrHuman': {'Simply Lift': 0, 'Iron Temple': 0, 'She Lifts': 0},
            'Spring Festival': {'Simply Lift': 0, 'Iron Temple': 0, 'She Lifts': 0},
            'Fall Classic': {'Simply Lift': 0, 'Iron Temple': 0, 'She Lifts': 0}
        }
        required_places = 7

        # when
        result = utils.update_booked_places(competition_name, club_name, booked_places, required_places)

        # then
        assert result == {
            'Push&Pull': {'Simply Lift': 7, 'Iron Temple': 0, 'She Lifts': 0},
            'MrHuman': {'Simply Lift': 0, 'Iron Temple': 0, 'She Lifts': 0},
            'Spring Festival': {'Simply Lift': 0, 'Iron Temple': 0, 'She Lifts': 0},
            'Fall Classic': {'Simply Lift': 0, 'Iron Temple': 0, 'She Lifts': 0}
        }
    
    def test_get_past_competitions(self):
        # given
        competitions = mocks.MOCK_COMPETITIONS

        # when
        result = utils.get_past_competitions(competitions)

        # then
        assert result == mocks.MOCK_PAST_COMPETITIONS
    
    def test_get_present_competitions(self):
        # given
        competitions = mocks.MOCK_COMPETITIONS

        # when
        result = utils.get_present_competitions(competitions)

        # then
        assert result == mocks.MOCK_PRESENT_COMPETITIONS