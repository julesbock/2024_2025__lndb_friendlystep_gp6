from flask import redirect, url_for, session
from data_show import *
from data import *
import json, os, calendar, random, string
from datetime import datetime, timedelta

def get_date(type):
    today = datetime.now()
    if type == "int":
        return {
            "current_year": today.year,
            "current_month": today.month,
            "current_day": today.day
        }
    elif type == "str":
        return {
            "current_year": str(today.year),
            "current_month": str(today.month),
            "current_day": str(today.day)
        }
        
def pj(*args):
    return os.path.join(*args)

def get_pfp():
    return os.path.dirname(__file__)

def get_conversations_folder_path():
    user_folder_path = get_user_folder_path()  
    conversations_folder_path = pj(user_folder_path, first_folder_name)
    return conversations_folder_path

def get_tournaments_players_file_path():
    tournaments_players_file_path = pj(get_tournament_data_folder_path(), "tournaments_players.json")
    return tournaments_players_file_path

def get_user_folder_path():
    user = session['name_user']
    users_folder_path = get_users_folder_path()
    user_folder_path = pj(users_folder_path, user)
    return user_folder_path

def get_users_folder_path():
    project_folder_path = get_pfp()
    users_folder_path = pj(project_folder_path, "data", "users")
    return users_folder_path  

def get_user_file_path(file_name):
    user_folder_path = get_user_folder_path()
    user_file_path = pj(user_folder_path, file_name)
    return user_file_path
    
def get_users_list_path():
    users_list_path = pj(get_users_folder_path(), "users_list.json")
    return users_list_path

def get_tournament_data_folder_path():
    project_folder_path = get_pfp()
    user_folder_path = pj(project_folder_path, "data", "tournaments_data")
    return user_folder_path

def get_tournaments_folder_path():
    tournament_data_folder_path = get_tournament_data_folder_path()
    tournaments_folder_path =  pj(tournament_data_folder_path, "tournaments")
    return tournaments_folder_path

def get_tournament_file_path(file_name):
    tournament_folder_path = get_tournaments_folder_path()
    tournament_file_path = pj(tournament_folder_path, file_name)
    return tournament_file_path

def load_data_from_file(file_path):
    if not os.path.exists(file_path) or os.stat(file_path).st_size == 0:
        return {}
    with open(file_path, 'r') as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return {}

def load_data_from_user_file(file_name):
    file_path = get_user_file_path(file_name)
    data = load_data_from_file(file_path)
    return data

def dump_data_in_file(file_path, data):
    directory = os.path.dirname(file_path)
    if not os.path.exists(directory):
        os.makedirs(directory)
    with open(file_path, 'w') as f:
        json.dump(data, f, indent=4)
        
def dump_data_in_user_file(file_name, data):
    file_path = get_user_file_path(file_name)
    dump_data_in_file(file_path, data)

def convert_to_decimal_hours(value):
    try:
        hours, minutes = map(int, value.split(":"))
        return hours + minutes / 60
    except ValueError:
        print(f"Erreur de conversion pour la valeur : {value}")
        return 0
    
def do_all_graphics(data_type, label):
    all_user_data = load_data_from_user_file("user_data.json")
    needed_data = {}
    current_year = get_date("int")["current_year"]
    previous_year = current_year - 1
    if str(current_year) in all_user_data:
        needed_data[str(current_year)] = all_user_data[str(current_year)]
    if str(previous_year) in all_user_data:
        needed_data[str(previous_year)] = all_user_data[str(previous_year)]
    data_of_the_seven_days_to_graph = get_last_seven_days_value(data_type, needed_data)
    data_of_the_month_to_graph = get_month_values(data_type, needed_data)
    data_of_the_year_to_graph= get_last_year_values(data_type, needed_data)
    create_graphics(label, data_of_the_seven_days_to_graph, data_of_the_month_to_graph, data_of_the_year_to_graph)
    
def create_graphics(label, data_of_the_seven_days_to_graph, data_of_the_month_to_graph, data_of_the_year_to_graph):
    create_seven_days_graph(label, data_of_the_seven_days_to_graph)
    print(data_of_the_month_to_graph)
    create_month_graph(label, data_of_the_month_to_graph)
    create_year_graph(label, data_of_the_year_to_graph)
    
def get_precise_day_value(data_type, all_data, year_month_day):
    year, month, day = year_month_day
    year_data = all_data.get(str(year), {})
    month_data = year_data.get(str(month), {})
    day_data = month_data.get(str(day), {})
    value = day_data.get(data_type, 0)
        # Si la valeur est au format hh:mm
    if isinstance(value, str) and ":" in value:
        # Conversion d'une valeur formatée en hh:mm (heures + minutes) en heures décimales
        return convert_to_decimal_hours(value)
    # Sinon, essayer de convertir en float normalement
    return float(str(value).lstrip("0") or "0")
    
def get_last_seven_days_value(data_type, all_data):
    today = datetime.now()
    lasts_days_values = []
    for i in range(6, -1, -1):
        day = today - timedelta(days=i)
        current_day = day.day
        year = day.year
        month = day.month
        value = get_precise_day_value(data_type, all_data, (year, month, current_day))
        lasts_days_values.append(value)   
    return lasts_days_values

def get_month_values(data_type, all_data, last_x_month=0):
    current_year, current_month, current_day = get_date("int").values()
    month_values = []
    the_month = current_month - last_x_month
    if the_month <= 0:
        the_month += 12
        current_year -= 1
    if last_x_month == 0:
        number_of_days_in_the_month = calendar.monthrange(current_year, current_month)[1]
        for day in range(1, current_day + 1):
            value=get_precise_day_value(data_type, all_data, (current_year, the_month, day))
            month_values.append(float(value))
    else:
        number_of_days_in_the_month = calendar.monthrange(current_year, the_month)[1]
        for day in range(1, number_of_days_in_the_month + 1):
            value=get_precise_day_value(data_type, all_data, (current_year, the_month, day))
            month_values.append(float(value))
    return month_values

def calculate_mean(list_values):
    if len(list_values) == 0:
        return 0
    return sum(list_values) / len(list_values)
    
def get_last_year_values(data_type, all_data):
    current_month = get_date("int")["current_month"]
    month_values = []
    for month in range(1, current_month +1 ):
        values_list = get_month_values(data_type, all_data, month)
        mean_value = calculate_mean(values_list)
        month_values.append(mean_value)
    return month_values

def check_if_data_exists(existing_data):
    current_year, current_month, current_day = get_date("str").values()
    if current_year in existing_data:
        if current_month in existing_data[current_year]:
            if current_day in existing_data[current_year][current_month]:
                # Si des données existent, récupérer celles-ci
                existing_data_for_today = existing_data[current_year][current_month][current_day]
            else:
                existing_data_for_today = {}
        else:
            existing_data_for_today = {}
    else:
        existing_data_for_today = {}
    return existing_data_for_today

def put_data_in_user_data(personnal_user_data): 
    all_data = load_data_from_user_file("user_data.json")
    current_year, current_month, current_day = get_date("str").values()
    all_data = check_if_all_good(all_data, current_year, current_month, current_day)
    all_data[current_year][current_month][current_day] = (personnal_user_data)
    dump_data_in_user_file("user_data.json", all_data)

def create_all_dates_dic():
    current_year, current_month, current_day = get_date("int").values()
    all_dates_dic = {}
    for year in range (2024, current_year + 1):
        all_dates_dic[year] = {}
        if year == current_year:
            for month in range(1, current_month + 1):
                all_dates_dic[year][month] = {}
                number_of_days_in_specific_month = calendar.monthrange(year, month)[1]
                if month == current_month : 
                    for day in range (1, current_day + 1):
                        all_dates_dic[year][month][day] = {}
                else :
                    for day in range(1, number_of_days_in_specific_month + 1):
                        all_dates_dic[year][month][day] = {}
        else : 
            for month in range(1, 13):
                all_dates_dic[year][month] = {}
                number_of_days_in_specific_month = calendar.monthrange(year, month)[1]
                for day in range(1, number_of_days_in_specific_month + 1):
                    all_dates_dic[year][month][day] = {}
    return all_dates_dic

def check_if_all_good(dic, current_year, current_month, current_day):
    dic.setdefault(str(current_year), {}).setdefault(str(current_month), {}).setdefault(str(current_day), {})
    return dic

def recherch_user(name_user, mdp):
    users_list_path = get_users_list_path()
    all_data = load_data_from_file(users_list_path)
    for user in all_data["users_list"]:
        if user["username"] == name_user and user["mdp"] == mdp:
            return user
    return None

def create_and_register_user(user_personnal_data):
    name = user_personnal_data["username"] 
    user_path = pj(get_users_folder_path(), name)
    if not os.path.exists(user_path):
        register_user(name, user_personnal_data['mdp'])
        create_user(user_personnal_data, user_path)
    else:
        pass
    return redirect(url_for("root.root"))

def create_user(user_personnal_data, user_path):
    os.mkdir(user_path)
    first_file_path = pj(user_path, first_file_name + ".json")
    second_file_path = pj(user_path, second_file_name + ".json")
    third_file_path = pj(user_path, third_file_name + ".json")
    first_folder_path = pj(user_path, first_folder_name)
    os.mkdir(first_folder_path)
    notifications = []
    the_dic = create_all_dates_dic()
    dump_data_in_file(first_file_path, user_personnal_data)
    dump_data_in_file(second_file_path, the_dic)
    dump_data_in_file(third_file_path, notifications)

def register_user(username, mdp):
    users_list_path = get_users_list_path()
    user_and_mdp = {
        "username" : username,
        "mdp" : mdp
    }
    all_data = load_data_from_file(users_list_path)
    all_data ["users_list"].append(user_and_mdp)
    dump_data_in_file(users_list_path, all_data)

def generate_tournament_id():
    tournament_id = "".join(random.choices(BASE32_ALPHABET, k=11))
    return tournament_id

def check_if_tournament_id_exists(tournament_id):
    file_path = get_tournament_file_path(f"{tournament_id}.json")
    return os.path.exists(file_path)
    
def get_unique_tournament_id():
    while True:
        tournament_id = generate_tournament_id()
        if not check_if_tournament_id_exists(tournament_id):
            return tournament_id

def save_tournament_data(tournament_id, tournament_data):
    tournaments_path = get_tournaments_folder_path()
    os.makedirs(tournaments_path, exist_ok=True)
    tournaments_participants__file_path = get_tournaments_players_file_path()
    data = load_data_from_file(tournaments_participants__file_path)
    data[tournament_id] = [session['name_user']]
    file_path = get_tournament_file_path(f"{tournament_id}.json")
    dump_data_in_file(tournaments_participants__file_path, data)
    try:
        dump_data_in_file(file_path, tournament_data)
    except Exception as e:
        error_message = f"Une erreur s'est produite lors de l'enregistrement du tournoi {tournament_id}: {e}"
        print(error_message)
        delete_tournament(tournament_id)
        return error_message
    
def delete_tournament(tournament_id):
    file_path = pj(get_tournaments_folder_path(), f"{tournament_id}.json")
    os.remove(file_path)

def search_tournament(tournament_id):
    tournaments_participants__file_path = get_tournaments_players_file_path()
    file_path = get_tournament_file_path(f"{tournament_id}.json")
    if os.path.exists(file_path):
        tournament_data = load_data_from_file(file_path)
        data = load_data_from_file(tournaments_participants__file_path)
        tournament_data['list_of_players'] = data[tournament_id]
        tournament_data['number_of_players'] = len(tournament_data['list_of_players'])
        return tournament_data
    else:
        return None
    
def get_player_category_data(category, player, start_date):
    user_path = pj(get_users_folder_path(), player, "user_data.json")
    all_data = load_data_from_file(user_path)
    start_date = datetime.strptime(start_date, "%Y-%m-%d")
    category_values = []
    for year, months in all_data.items():
        for month, days in months.items():
            for day, data in days.items():
                month = int(month)
                day = int(day)
                day_date_str = f"{year}-{month:02d}-{day:02d}"
                day_date = datetime.strptime(day_date_str, "%Y-%m-%d")
                if day_date >= start_date:
                    category_value = data.get(category, 0)
                    if isinstance(category_value, str) and ":" in category_value:
                        category_values.append(convert_to_decimal_hours(category_value))
                    else:
                        category_values.append(float(str(category_value).lstrip("0") or "0"))

    # Calculer la moyenne des valeurs
    return calculate_mean(category_values)

def sort_dic_by_value(dico):
    return dict(sorted(dico.items(), key=lambda x: x[1], reverse=True))
    
def do_tournament_graphic(category, list_of_players, start_date):
    player_data = {}
    for player in list_of_players:
        player_data[player] = get_player_category_data(category, player, start_date)
    player_data = sort_dic_by_value(player_data)
    print(player_data)
    create_tournament_graphic(player_data, category)

def create_notif(object, sender, receiver, tournament_id):
    notif = make_notif(object, sender, receiver, tournament_id)
    save_notif(notif, receiver)
    
def make_notif(object, sender, receiver, tournament_id):
    current_datetime = datetime.now()
    date = current_datetime.date().isoformat() 
    sent_at_hour = current_datetime.strftime("%H:%M") 
    notif = {
        "sender": sender,
        "receiver": receiver,
        "object": message_object.get(object, ""),
        "sent_at_date": date,
        "sent_at_hour": sent_at_hour,
        "content": f"{sender.title()}, {message_content.get(object, '')}"
    }
    if object == "invitation_to_a_tournament" or object == "tournament_entry_request":
        notif["tournament_id"] = tournament_id
    return notif

def save_notif(notif, user):
    user_notification_path = pj(get_users_folder_path(), user, "user_notifications.json")
    all_data = load_data_from_file(user_notification_path)
    all_data.append(notif)
    dump_data_in_file(user_notification_path, all_data)
        
        
# ajouter le noùm du tournoi de l invit + min caractere pour mdp, changer la couleur pour dire que l invitation a ete envoyée, 
# apparition comme une notif si envoyé recemement + icone 3 nouvelles notifs ...