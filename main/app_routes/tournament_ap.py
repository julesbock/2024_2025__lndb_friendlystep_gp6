from flask import render_template, request, redirect, url_for, Blueprint, session
import os, json

tournaments_blueprint = Blueprint('tournaments', __name__, url_prefix='/tournaments')

@tournaments_blueprint.route('/')
def tournaments():
    return render_template('tournaments.html')

@tournaments_blueprint.route('/create', methods = ["POST", "GET"])
def create_tournament():
    if request.method == 'POST':
        name= request.form.get('name')
        date= request.form.get('date')
        duration= request.form.get('duration')

        tournament_data= {
            "name": name,
            "date": date,
            "duration": duration,
            "created_by": session.get('username')}
        
        save_tournament_data(name, tournament_data)

        return redirect(url_for('tournaments.tournaments'))
    return render_template('create_tournament.html')

@tournaments_blueprint.route('/join', methods = ["POST", "GET"])
def join_tournament():
    if request.method == 'POST':
        return redirect(url_for('tournaments.tournaments'))
    return render_template('join_tournament.html')

@tournaments_blueprint.route('/<int:tournament_id>')
def view_tournament(tournament_id):
    return f"Voir les détails du tournoi {tournament_id}"


def save_tournament_data(tournament_name, tournament_data):
    file_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'tournaments.json')

    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            data = json.load(file)
    else:
        data = {}

    data[tournament_name] = tournament_data

    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)