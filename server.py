import json

from flask import Flask, render_template, request, redirect, flash, url_for

import utils


def load_clubs():
    with open('clubs.json') as clubs_json:
         return json.load(clubs_json)['clubs']


def load_competitions():
    with open('competitions.json') as competitions_json:
         return json.load(competitions_json)['competitions']


app = Flask(__name__)
app.secret_key = 'something_special'


CLUBS = load_clubs()
COMPETITIONS = load_competitions()

PAST_COMPETITIONS = utils.get_past_competitions(COMPETITIONS)
PRESENT_COMPETITIONS = utils.get_present_competitions(COMPETITIONS)

BOOKED_PLACES = utils.initialize_booked_places(COMPETITIONS, CLUBS)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/show-summary', methods=['POST'])
def show_summary():
    email = request.form.get('email', "")
    if not email:
        flash("Please enter your email.", 'error')
        return render_template('index.html'), 401

    club = [club for club in CLUBS if club['email'] == email]

    if club:
        return render_template(
            'welcome.html',
            club=club[0],
            past_competitions=PAST_COMPETITIONS,
            present_competitions=PRESENT_COMPETITIONS
        )

    flash(f"No account related to this email: {email}.", 'error')
    return render_template('index.html'), 401


@app.route('/book/<competition_name>/<club_name>')
def book(competition_name, club_name):
    found_club = [club for club in CLUBS if club['name'] == club_name]
    if not found_club:
        flash(f"There is no club with the name {club_name}.", 'error')
        return render_template('index.html'), 404

    found_competition = [competition for competition in COMPETITIONS if competition['name'] == competition_name]
    if not found_competition:
        flash(f"There is no competition with the name {competition_name}.", 'error')
        status_code = 404
    
    elif found_competition[0] in PAST_COMPETITIONS:
        flash(f"The competition {found_competition[0]['name']} is over.", 'error')
        status_code = 400
    
    else:
        return render_template('booking.html', club=found_club[0], competition=found_competition[0])
    
    return render_template(
            'welcome.html',
            club=found_club[0],
            past_competitions=PAST_COMPETITIONS,
            present_competitions=PRESENT_COMPETITIONS
        ), status_code

@app.route('/purchase-places', methods=['POST'])
def purchase_places():
    club = [club for club in CLUBS if club['name'] == request.form['club']][0]
    competition = [competition for competition in COMPETITIONS if competition['name'] == request.form['competition']][0]

    required_places = int(request.form['places'])
    competition_places = int(competition['numberOfPlaces'])
    club_points = int(club['points'])

    if not (0 < required_places < 13):
        flash("Please enter a valid number (between 1 and 12).", 'error')
    
    elif required_places > competition_places:
        flash(f"There are only {competition_places} places available.", 'error')
    
    elif not utils.check_club_places(competition['name'], club['name'], BOOKED_PLACES, required_places):
        flash("You cannot book more than 12 places in a competition.", 'error')
    
    elif required_places * 3 > club_points:
        flash(f"You do not have enough points: {required_places * 3 - club_points} points missing.")
    
    else:
        utils.update_booked_places(competition['name'], club['name'], BOOKED_PLACES, required_places)
        competition['numberOfPlaces'] = competition_places - required_places
        club['points'] = club_points - (required_places * 3)
        flash('Great-booking complete!', 'success')
        return render_template(
            'welcome.html',
            club=club,
            past_competitions=PAST_COMPETITIONS,
            present_competitions=PRESENT_COMPETITIONS
        )
    return render_template('booking.html', club=club, competition=competition), 400


# TODO: Add route for points display


@app.route('/logout')
def logout():
    return redirect(url_for('index'))