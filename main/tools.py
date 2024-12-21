from flask import Flask, render_template, request, redirect, url_for, session
from app import *
from data import *
import json, os

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
    with open(chemin_second_file, "w") as json_file:
        json.dump(None, json_file, indent=4)
    

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