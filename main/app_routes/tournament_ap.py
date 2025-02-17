from flask import render_template, request, redirect, url_for, Blueprint, session, flash
from main_tools import *
from datetime import datetime, timedelta

tournaments_blueprint = Blueprint('tournaments', __name__, url_prefix='/tournaments')

@tournaments_blueprint.route('/')
def tournaments():
# Lire les données des tournois à partir des fichiers JSON
    tournaments_folder_dir = os.path.join(os.path.dirname(__file__), '..', 'data', 'tournaments_data')
    tournaments_dir = os.path.join(tournaments_folder_dir, "tournaments")
    another_dir = os.path.join(tournaments_folder_dir, "tournaments_players.json")
    tournaments = []
    with open(another_dir, 'r') as f:
        data = json.load(f)
    user_tournaments = [key for key, players in data.items() if session['name_user'] in players]
    if os.path.exists(tournaments_dir):
        for filename in os.listdir(tournaments_dir):
            if filename.endswith('.json'):
                file_path = os.path.join(tournaments_dir, filename)
                with open(file_path, 'r') as file:
                    tournament = json.load(file)
                if tournament['id'] in user_tournaments:
                    participants = data.get(tournament['id'], [])
                    nb_of_participants = len(participants)
                    tournament['number_of_participants'] = nb_of_participants
                    tournaments.append(tournament)

    # Classer les tournois en fonction de leur date et durée
    current_date = datetime.now().date()
    ongoing_tournaments = []
    upcoming_tournaments = []
    past_tournaments = []

    for tournament in tournaments:
        
        if 'start_date' in tournament and 'duration' in tournament:
            start_date = datetime.strptime(tournament['start_date'], '%Y-%m-%d').date()
            end_date = datetime.strptime(tournament['end_date'], '%Y-%m-%d').date()

            if end_date < current_date:
                past_tournaments.append(tournament)
            elif start_date <= current_date <= end_date:
                ongoing_tournaments.append(tournament)
            else:
                upcoming_tournaments.append(tournament)

    return render_template(
        'tournaments/tournaments.html', 
        ongoing_tournaments=ongoing_tournaments, 
        upcoming_tournaments=upcoming_tournaments, 
        past_tournaments=past_tournaments
    )

@tournaments_blueprint.route('/create', methods = ["POST", "GET"])
def create_tournament():
    if request.method == 'POST':
        name = request.form.get('name')
        date = request.form.get('date')
        duration = request.form.get('duration')
        category = request.form.get('category')
        tournament_id = get_unique_tournament_id()
        start_date = datetime.strptime(date, '%Y-%m-%d').date()
        end_date = (start_date + timedelta(days=int(duration))).isoformat()
        tournament_data= {
            "id" : tournament_id,
            "name": name,
            "category": category,
            "start_date": date,
            "duration": duration,
            "end_date": end_date,
            "created_by": session.get('name_user'),
            }
        error = save_tournament_data(tournament_id, tournament_data)
        if error:
            flash(error, "error")
            return redirect(url_for('tournaments.create_tournament'))
        elif check_if_tournament_id_exists(tournament_id):
            flash("Tournoi créé avec succès !", "success")
        return redirect(url_for('tournaments.tournaments'))
    return render_template('tournaments/create_tournament.html')

@tournaments_blueprint.route('/join', methods = ["POST", "GET"])
def join_tournament():
    if request.method == 'POST':
        tournament_id = request.form.get('tournament_id')
        if check_if_tournament_id_exists(tournament_id):
            path = os.path.dirname(__file__)
            another_path = os.path.join(path, "..",  "data", "tournaments_data", "tournaments_players.json")
            with open(another_path, 'r') as f:
                another_data = json.load(f)
            user = session['name_user']
            print(user)
            if user not in another_data[tournament_id]:
                another_data[tournament_id].append(user)
                print(user)
            with open(another_path, "w") as f:
                json.dump(another_data, f, indent=4)
            return redirect(url_for('tournaments.view_tournament', tournament_id=tournament_id))
        else:
            error_type = "tournament_nf"
            return redirect(url_for('errors.error', error_type=error_type))
    return render_template('tournaments/join_tournament.html')

@tournaments_blueprint.route('/view/<tournament_id>')
def view_tournament(tournament_id):
    tournament_data = search_tournament(tournament_id)
    if not tournament_data:
        flash(f"Le tournoi {tournament_id} n'existe pas", "error")
        return redirect(url_for('tournaments.join_tournament'))
    return render_template('tournaments/view_tournament.html', tournament_data=tournament_data)

@tournaments_blueprint.route('/tournament/<tournament_id>')
def tournament_page(tournament_id):
    tournament_data = search_tournament(tournament_id)
    category = tournament_data['category']
    start_date = tournament_data['start_date']
    list_of_the_participants = tournament_data['list_of_players']
    do_tournament_graphic(category, list_of_the_participants, start_date)
    return render_template("tournaments/tournament_page.html", tournament_data=tournament_data)