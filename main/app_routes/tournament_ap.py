from flask import render_template, request, redirect, url_for, Blueprint, session, flash
from main_tools import *

tournaments_blueprint = Blueprint('tournaments', __name__, url_prefix='/tournaments')

@tournaments_blueprint.route('/')
def tournaments():
    return render_template('tournaments/tournaments.html')

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
        if tournament_data:
            return redirect(url_for('tournaments.view_tournament', tournament_id=tournament_id))
        else:
            flash(f"Le tournoi {tournament_id} n'existe pas", "error")
        return redirect(url_for('tournaments.tournaments'))
    return render_template('tournaments/join_tournament.html')

@tournaments_blueprint.route('/view/<tournament_id>')
def view_tournament(tournament_id):
    tournament_data = search_tournament(tournament_id)
    if not tournament_data:
        flash(f"Le tournoi {tournament_id} n'existe pas", "error")
        return redirect(url_for('tournaments.join_tournament'))
    return render_template('tournaments/view_tournament.html', tournament_data=tournament_data)

