from flask import Flask, render_template, request, redirect, url_for, session
from app import *
from data import *
import json, os, datetime, calendar

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

def put_data_in_user_data(personnal_user_data): 
    all_data = get_data("user_data.json")
    date_heure = datetime.datetime.now()
    current_year = str(date_heure.year)
    current_month = str(date_heure.month)
    current_day = str(date_heure.day)
    all_data = check_if_all_good(all_data, current_year, current_month, current_day)
    all_data ["user_data"][current_year][current_month][current_day] = (personnal_user_data)
    give_data("user_data.json", all_data)

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
