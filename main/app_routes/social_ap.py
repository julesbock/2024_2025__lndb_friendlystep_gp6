from flask import Blueprint, render_template, session, request, jsonify
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

@social_blueprint.route('/messaging', methods=["POST", "GET"])
def messaging():
    user = session.get('name_user')
    if not user:
        return "Utilisateur non authentifié", 403
    error = ""
    conversations_folder = get_conversations_folder_path()
    all_conversations = os.listdir(conversations_folder)
    conversations_dict = {}  
    for filename in all_conversations:
        file_path = pj(conversations_folder, filename)
        if os.path.isfile(file_path):
            with open(file_path, "r", encoding="utf-8") as file:
                try:
                    conversations_dict[filename] = json.load(file) 
                except json.JSONDecodeError:
                    conversations_dict[filename] = []
    if request.method == "POST":
        print('hiiiiii')
        username = request.form.get('name_of_the_user', None)
        print(username)
        users_list_path = get_users_list_path()
        data = load_data_from_file(users_list_path)
        if username:
            if username == user:
                error = "Vous ne pouvez pas vous envoyer de message à vous-même."
            elif any(user['username'] == username for user in data["users_list"]):
                file_name = f'{username}.json'
                if file_name in all_conversations:
                    error = "Vous avez déjà une conversation avec cet utilisateur."
                else:
                    conversation_path_for_user = pj(conversations_folder, file_name)
                    initial_message = [{
                        "sender": user,
                        "message": "Conversation started!",
                        "hour": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    }]
                    conversation_folder_of_other_user = pj(get_users_folder_path(), username)
                    conversation_path_for_other_user = pj(conversation_folder_of_other_user, "conversations", f'{user}.json')
                    dump_data_in_file(conversation_path_for_other_user, initial_message)
                    dump_data_in_file(conversation_path_for_user, initial_message)
                    error = "Conversation créée avec succès!"
            else:
                error = "Cet utilisateur n'existe pas."
                                
    return render_template('user_data/messaging.html', conversations=conversations_dict, error=error)


