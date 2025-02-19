from flask import Blueprint, render_template, session, request
from main_tools import *

social_blueprint = Blueprint('social', __name__, url_prefix='/social')

@social_blueprint.route('/')
def social():
    return render_template('user_data/social.html')

@social_blueprint.route('/notifications')
def notifications():
    if "&amp;" in request.url:
        corrected_url = request.url.replace("&amp;", "&")
        return redirect(corrected_url)
    user = session.get('name_user')
    if not user:
        return "Utilisateur non authentifié", 403
    chemin = os.path.dirname(__file__)
    true_path = os.path.join(chemin, "..", "data", "users", user, "user_notifications.json")

    # Vérification si le fichier existe
    if not os.path.exists(true_path):
        all_data = []
    else:
        with open(true_path, "r") as f:
            try:
                all_data = json.load(f)
            except json.JSONDecodeError:
                all_data = []

    invitations_and_requests = [
        "You are invited to a tournament!",
        "Tournament entry request",
        "New friend request"
    ]
    index = request.args.get('index', None)
    response = request.args.get('response', None)
    print("hi")
    print(index)
    print(response)

    if index and response : 
        print("hi")
        index = int(index)
        if response == "Yes" : 
            print("hi")
            notification = all_data[index]
            sender = notification["sender"]
            receiver = notification["receiver"]
            tournament_id = notification['tournament_id']
            path = os.path.join(os.path.dirname(__file__), "..", "data", "tournaments_data", "tournaments_players.json")
            with open(path, 'r') as f:
                lists_of_players = json.load(f)
            if sender in lists_of_players[tournament_id]:
                lists_of_players[tournament_id].append(receiver)
            else:
                lists_of_players[tournament_id].append(sender)
            with open(path, 'w') as f:
                json.dump(lists_of_players, f, indent=4)
        elif response == "No":
            #variable de reponse aux notif (arg no)
            pass
        del all_data[index]
        with open(true_path, 'w') as f:
            json.dump(all_data, f, indent=4)     
        return redirect(url_for('social.notifications'))          
    return render_template(
        'user_data/notifications.html',
        notifications=all_data,
        invitations_and_requests=invitations_and_requests
    )

