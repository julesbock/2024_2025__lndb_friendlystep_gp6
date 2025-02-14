from flask import render_template, request, redirect, url_for, Blueprint, session, flash
from main_tools import *
from datetime import datetime, timedelta

tournaments_blueprint = Blueprint('tournaments', __name__, url_prefix='/tournaments')

@tournaments_blueprint.route('/')
def tournaments():
# Lire les données des tournois à partir des fichiers JSON
    tournaments_dir = os.path.join(os.path.dirname(__file__), '..', 'tournaments')
    tournaments = []

    if os.path.exists(tournaments_dir):
        for filename in os.listdir(tournaments_dir):
            if filename.endswith('.json'):
                file_path = os.path.join(tournaments_dir, filename)
                with open(file_path, 'r') as file:
                    tournament = json.load(file)
                    tournaments.append(tournament)

    # Classer les tournois en fonction de leur date et durée
    current_date = datetime.now().date()
    ongoing_tournaments = []
    upcoming_tournaments = []
    past_tournaments = []

    for tournament in tournaments:
        if 'date' in tournament and 'duration' in tournament:
            start_date = datetime.strptime(tournament['date'], '%Y-%m-%d').date()
            end_date = start_date + timedelta(days=int(tournament['duration']))
            tournament['end_date'] = end_date.strftime('%Y-%m-%d')
            if end_date < current_date:
                 past_tournaments.append(tournament)
            elif start_date <= current_date <= end_date:
                 ongoing_tournaments.append(tournament)
            else:
                upcoming_tournaments.append(tournament)

    return render_template('tournaments/tournaments.html', ongoing_tournaments=ongoing_tournaments, upcoming_tournaments=upcoming_tournaments, past_tournaments=past_tournaments)

@tournaments_blueprint.route('/create', methods = ["POST", "GET"])
def create_tournament():
    if request.method == 'POST':
        name= request.form.get('name')
        date= request.form.get('date')
        duration= request.form.get('duration')
        tournament_id = get_unique_tournament_id()
        tournament_data= {
            "id" : tournament_id,
            "name": name,
            "date": date,
            "duration": duration,
            "created_by": session.get('username')}
        error = save_tournament_data(tournament_id, tournament_data)
        if error:
            flash(error, "error")
            return redirect(url_for('tournaments.create_tournament'))
        else :
            flash("Tournoi créé avec succès !", "success")
        return redirect(url_for('tournaments.tournaments'))
    return render_template('tournaments/create_tournament.html')

@tournaments_blueprint.route('/join', methods = ["POST", "GET"])
def join_tournament():
    if request.method == 'POST':
        tournament_id = request.form.get('tournament_id')
        tournament_data = search_tournament(tournament_id)
        if check_if_tournament_id_exists(tournament_id) == True:
            return redirect(url_for('tournaments.view_tournament', tournament_id=tournament_id))
        else:
            error_type = "tournament_nf"
            return redirect(url_for('errors.error', error_type=error_type))
        return redirect(url_for('tournaments.tournaments'))
    return render_template('tournaments/join_tournament.html')

@tournaments_blueprint.route('/view')
def view_tournament(tournament_id):
    tournament_data = search_tournament(tournament_id)
    if not tournament_data:
        flash(f"Le tournoi {tournament_id} n'existe pas", "error")
        return redirect(url_for('tournaments.join_tournament'))
    return render_template('tournaments/view_tournament.html', tournament_data=tournament_data)

