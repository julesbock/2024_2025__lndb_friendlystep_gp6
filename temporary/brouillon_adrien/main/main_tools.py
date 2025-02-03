from flask import redirect, url_for, session
from data_show import *
import json, os, datetime, calendar

# Fonctions root



# Fonctions de gestion de données des utilisateurs
def do_all_graphics(data_type, label):
    all_user_data = get_data("user_data.json")
    needed_data = {}
    # Récupérer les données pour les années 2024 et 2025
    if "2024" in all_user_data["user_data"]:
        needed_data["2024"] = all_user_data["user_data"]["2024"]
    if "2025" in all_user_data["user_data"]:
        needed_data["2025"] = all_user_data["user_data"]["2025"]
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
    """
    Récupère la valeur associée à un type de données spécifique pour une date précise.

    Args:
        data_type (str): Le type de données à récupérer (par exemple, "step_data").
        all_data (dict): Le dictionnaire contenant toutes les dates et leurs valeurs associées.
        year_month_day (tuple): Un tuple contenant l'année, le mois et le jour pour la date précise.

    Returns:
        int: La valeur associée au type de données spécifié pour la date précise.
    """
    year, month, day = year_month_day
    year = str(year)
    month = str(month)
    day = str(day)

    if year in all_data and month in all_data[year] and day in all_data[year][month]:
        return float(str(all_data[year][month][day].get(data_type, 0)).lstrip("0") or "0")
    return 0

def get_last_seven_days_value(data_type, all_data):
    today = datetime.datetime.now()
    lasts_days_values = []
    
    for i in range(7):
        day = today - datetime.timedelta(days=i)
        current_day = day.day
        year = day.year
        month = day.month
       
        value = get_precise_day_value(data_type, all_data, (year, month, current_day))
        lasts_days_values.append(value)
            
    return lasts_days_values

def get_month_values(data_type, all_data, last_x_month=0):
    """
    Récupère les valeurs associées à un type de données spécifique pour le mois en cours jusqu'à la date actuelle,
    et pour les mois précédents spécifiés par last_x_month.

    Args:
        data_type (str): Le type de données à récupérer (par exemple, "step_data").
        all_data (dict): Le dictionnaire contenant toutes les dates et leurs valeurs associées.
        last_x_month (int): Le nombre de mois précédents à inclure dans les valeurs récupérées.

    Returns:
        list: Une liste contenant les valeurs pour le mois en cours jusqu'à la date actuelle et les mois précédents spécifiés.
    """
    today = datetime.datetime.now()
    current_year = today.year
    current_month = today.month
    current_day = today.day
    month_values = []
    the_month = current_month-last_x_month
    if the_month == 0:
        the_month = 12
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
    """
    Calcule la moyenne des valeurs dans une liste.

    Args:
        list_values (list): Une liste de valeurs numériques.

    Returns:
        float: La moyenne des valeurs dans la liste.
    """
    if len(list_values) == 0:
        return 0
    return sum(list_values) / len(list_values)
    
        
def get_last_year_values(data_type, all_data):
    today = datetime.datetime.now()
    current_month = int(today.month)
    month_values = []
    for month in range(current_month + 1):
        values_list = get_month_values(data_type, all_data, month)
        mean_value = calculate_mean(values_list)
        month_values.append(mean_value)

        
    return month_values

def get_data (file_wanted):
    dossier_projet = os.path.dirname(__file__)
    chemin_user = os.path.join(dossier_projet, "users", session["name_user"])
    chemin_file = os.path.join(chemin_user, file_wanted)
    with open(chemin_file, "r") as json_file:
        all_data = json.load(json_file)
    return all_data

def give_data(file_wanted, data):
    dossier_projet = os.path.dirname(__file__)
    chemin_user = os.path.join(dossier_projet, "users", session["name_user"])
    chemin_file = os.path.join(chemin_user, file_wanted)
    with open(chemin_file, "w") as json_file:
        json.dump(data, json_file, indent=4)

def check_if_data_exists(existing_data):
    date_time = datetime.datetime.now()
    current_year = str(date_time.year)
    current_month = str(date_time.month)
    current_day = str(date_time.day)
    if current_year in existing_data["user_data"]:
        if current_month in existing_data["user_data"][current_year]:
            if current_day in existing_data["user_data"][current_year][current_month]:
                # Si des données existent, récupérer celles-ci
                existing_data_for_today = existing_data["user_data"][current_year][current_month][current_day]
            else:
                existing_data_for_today = {}
        else:
            existing_data_for_today = {}
    else:
        existing_data_for_today = {}
    return existing_data_for_today

def put_data_in_user_data(personnal_user_data): 
    all_data = get_data("user_data.json")
    date_heure = datetime.datetime.now()
    current_year = str(date_heure.year)
    current_month = str(date_heure.month)
    current_day = str(date_heure.day)
    all_data = check_if_all_good(all_data, current_year, current_month, current_day)
    all_data ["user_data"][current_year][current_month][current_day] = (personnal_user_data)
    give_data("user_data.json", all_data)

def create_all_dates_dic():
    """
    Crée un dictionnaire contenant toutes les dates depuis l'année 2000 jusqu'à aujourd'hui.
    
    Structure :
    {
        année: {
            mois: {
                jour: {}
            }
        }
    }

    - Chaque jour est une clé avec un dictionnaire vide comme valeur.
    - Les années passées incluent tous les mois et jours.
    - L'année en cours inclut uniquement les mois jusqu'au mois actuel et les jours jusqu'au jour actuel.
    
    Returns:
        dict: Le dictionnaire contenant toutes les dates.
    """
    date_heure = datetime.datetime.now()
    current_year = date_heure.year
    current_month = date_heure.month
    current_day = date_heure.day
    all_dates_dic = {}
    all_dates_dic["user_data"] = {}
    for year in range (2000, current_year + 1):
        all_dates_dic["user_data"][year] = {}
        if year == current_year:
            for month in range(1, current_month + 1):
                all_dates_dic["user_data"][year][month] = {}
                number_of_days_in_specific_month = calendar.monthrange(year, month)[1]
                if month == current_month : 
                    for day in range (1, current_day + 1):
                        all_dates_dic["user_data"][year][month][day] = {}
                else :
                    for day in range(1, number_of_days_in_specific_month + 1):
                        all_dates_dic["user_data"][year][month][day] = []
        else : 
            for month in range(1, 13):
                all_dates_dic["user_data"][year][month] = {}
                number_of_days_in_specific_month = calendar.monthrange(year, month)[1]
                for day in range(1, number_of_days_in_specific_month + 1):
                    all_dates_dic["user_data"][year][month][day] = {}
    return all_dates_dic

# Fonctions de gestion des utilisateurs

def check_if_all_good(dic, current_year, current_month, current_day):
    dic.setdefault('user_data', {}).setdefault(current_year, {}).setdefault(current_month, {}).setdefault(current_day, {})
    return dic

def recherch_user(name_user, mdp):
    dossier_projet = os.path.dirname(__file__)
    chemin_users_list = os.path.join(dossier_projet, "users", "users_list.json")
    with open(chemin_users_list, "r") as json_file:
            all_data = json.load(json_file)
    for user in all_data["users_list"]:
        if user["username"] == name_user and user["mdp"] == mdp:
            return user
    return None

def create_and_register_user(user_personnal_data):
    name = user_personnal_data["username"] 
    dossier_projet = os.path.dirname(__file__)
    chemin_users = os.path.join(dossier_projet, "users", name)
    if not os.path.exists(chemin_users):
        create_user(user_personnal_data, chemin_users)
        register_user(name, user_personnal_data['mdp'], dossier_projet)
    else:
        pass
    return redirect(url_for("root"))

def create_user(user_personnal_data, chemin_users):
    os.mkdir(chemin_users)
    first_file_name = "personnal_data"
    second_file_name = "user_data"
    chemin_first_file = os.path.join(chemin_users, first_file_name + ".json")
    chemin_second_file = os.path.join(chemin_users, second_file_name + ".json")
    with open(chemin_first_file, "w") as json_file:
        json.dump(user_personnal_data, json_file, indent=4)
    the_dic = create_all_dates_dic()
    with open(chemin_second_file, "w") as json_file:
        json.dump(the_dic, json_file, indent=4)   

def register_user(username, mdp, chemin_projet):
    chemin_users_list = os.path.join(chemin_projet, "users", "users_list.json")
    user_and_mdp = {
        "username" : username,
        "mdp" : mdp
    }
    with open(chemin_users_list, "r") as json_file:
        all_data = json.load(json_file)
    all_data ["users_list"].append(user_and_mdp)
    with open(chemin_users_list, "w") as json_file:
        json.dump(all_data, json_file, indent=4)
