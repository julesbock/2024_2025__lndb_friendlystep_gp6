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
    user_notification_path = get_user_notifications_path()
    if not os.path.exists(user_notification_path):
        all_data = []
    else:
        all_data = load_data_from_file(user_notification_path)
    all_data = check_if_all_data_tournaments_exist(all_data)
    dump_data_in_file(user_notification_path, all_data)
    index = request.args.get('index', None)
    response = request.args.get('response', None)
    if index and response : 
        index = int(index)
        if response == "Yes" : 
            notification = all_data[index]
            sender = notification["sender"]
            receiver = notification["receiver"]
            tournament_id = notification['tournament_id']
            tournaments_players_path = get_tournaments_players_file_path()
            lists_of_players = load_data_from_file(tournaments_players_path)
            if sender in lists_of_players[tournament_id]:
                lists_of_players[tournament_id].append(receiver)
            else:
                lists_of_players[tournament_id].append(sender)
            dump_data_in_file(tournaments_players_path, lists_of_players)
        elif response == "No":
            pass
        del all_data[index]
        dump_data_in_file(user_notification_path, all_data)
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
        username = request.form.get('name_of_the_user', None)
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