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
    email = request.form.get('email', "")
    if not email:
        flash("Please enter your email.", 'error')
        return render_template('index.html'), 401

    club = [club for club in CLUBS if club['email'] == email]

    if club:
        return render_template('welcome.html', club=club[0], competitions=COMPETITIONS)

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
        return render_template('welcome.html', club=found_club[0], competitions=COMPETITIONS), 404

    return render_template('booking.html', club=found_club[0], competition=found_competition[0])

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