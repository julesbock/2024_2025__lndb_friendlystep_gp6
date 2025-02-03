from flask import render_template, request, redirect, url_for, Blueprint, session
from main_tools import save_tournament_data

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

