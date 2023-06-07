import json

from flask import Flask, render_template, request, redirect, flash, url_for


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


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/show-summary', methods=['POST'])
def show_summary():
    club = [club for club in CLUBS if club['email'] == request.form['email']][0]
    return render_template('welcome.html', club=club, competitions=COMPETITIONS)


@app.route('/book/<competition_name>/<club_name>')
def book(competition_name, club_name):
    found_club = [club for club in CLUBS if club['name'] == club_name][0]
    found_competition = [competition for competition in COMPETITIONS if competition['name'] == competition_name][0]

    if found_club and found_competition:
        return render_template('booking.html', club=found_club, competition=found_competition)

    flash("Something went wrong. Please try again.")
    return render_template('welcome.html', club=found_club, competitions=COMPETITIONS)


@app.route('/purchase-places', methods=['POST'])
def purchase_places():
    club = [club for club in CLUBS if club['name'] == request.form['club']][0]
    competition = [competition for competition in COMPETITIONS if competition['name'] == request.form['competition']][0]

    places_required = int(request.form['places'])
    competition['numberOfPlaces'] = int(competition['numberOfPlaces']) - places_required

    flash('Great-booking complete!')
    return render_template('welcome.html', club=club, competitions=COMPETITIONS)


# TODO: Add route for points display


@app.route('/logout')
def logout():
    return redirect(url_for('index'))