from datetime import datetime
import json


def initialize_booked_places(competitions, clubs):
    booked_places = {}
    for competition in competitions:
        booked_places[f"{competition['name']}"] = {}

        for club in clubs:
            booked_places[f"{competition['name']}"].update({f"{club['name']}": 0})

    return booked_places


def check_club_places(competition_name, club_name, booked_places, required_places):
    places_booked_by_club = booked_places[competition_name][club_name]

    if places_booked_by_club + required_places > 12:
        return False

    return True


def update_booked_places(competition_name, club_name, booked_places, required_places):
    booked_places[competition_name][club_name] += required_places
    return booked_places


def get_past_competitions(competitions):
    return [
        competition
        for competition in competitions
        if datetime.strptime(competition['date'], '%Y-%m-%d %H:%M:%S') < datetime.now()
    ]


def get_present_competitions(competitions):
    return [
        competition
        for competition in competitions
        if datetime.strptime(competition['date'], '%Y-%m-%d %H:%M:%S') >= datetime.now()
    ]


def load_clubs():
    with open('clubs.json') as clubs_json:
         return json.load(clubs_json)['clubs']


def load_competitions():
    with open('competitions.json') as competitions_json:
         return json.load(competitions_json)['competitions']
