from app import *
from data import *

def recherch_user(name_user, mdp):
    for user in users:
        if user["nom"] == name_user and user["mdp"] == mdp:
            return user
    return None

def create_user(user_personnal_data): #user_personal_data est la récupération des données et doit être un dictionnaire afin de placer dans le fichier json le dico
    name = user_personnal_data["name"]  # Récupère le nom de l'utilisateur
    dossier_projet = os.path.dirname(__file__)
    # Chemin du dossier 'users'
    chemin_users = os.path.join(dossier_projet, "users", name)
    print(chemin_users)
    # Crée le dossier s'il n'existe pas déjà
    if not os.path.exists(chemin_users):
        os.mkdir(chemin_users)
        first_file_name = "personnal_data"
        second_file_name = "user_data"
        chemin_first_file = os.path.join(chemin_users, first_file_name + ".json")
        chemin_second_file = os.path.join(chemin_users, second_file_name + ".json")
        with open(chemin_first_file, "w") as json_file:
            json.dump(user_personnal_data, json_file, indent=4)
        with open(chemin_second_file, "w") as json_file:
            json.dump(user_personnal_data, json_file, indent=4)
        print(f"Dossier pour {name} créé à : {chemin_users}")
    else:
        print(f"Le dossier pour {name} existe déjà.")