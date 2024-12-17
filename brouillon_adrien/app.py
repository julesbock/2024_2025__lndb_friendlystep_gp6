from flask import Flask, render_template, request, redirect, url_for, session
import datetime
import os, json

app = Flask(__name__)
app.secret_key = "02458d8b8e67adc5966be5f1b3e109341e2507abfd007fa2785cde99996611e5"

@app.route('/')
def homepage():
    return render_template("homepage.html")


users = [
    {"nom" : 'admin', "mdp":"1234"},
    {"nom" : 'marie', "mdp":"nsi"},
    {"nom" : 'paul', "mdp":"azerty"}
]


def recherch_user(name_user, mdp):
    for user in users:
        if user["nom"] == name_user and user["mdp"] == mdp:
            return user
    return None


def create_user(user_personnal_data): #user_personal_data est la récupération des données et doit être un dictionnaire afin de placer dans le fichier json le dico
    name = user_personnal_data[0]  # Récupère le nom de l'utilisateur
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
    


@app.route('/login',  methods=["POST", "GET"])
def login():
    if request.method == "POST":
        # print(request.args)
        donnees = request.form
        nom = donnees.get('nom')
        mdp = donnees.get('mdp')
        user=recherch_user(nom, mdp)
        if user is not None:
            print('utilisateur trouvé')
            session["name_user"] = user['nom']
            print(session)
            return redirect(url_for('homepage'))
        else:
            print('utilisateur inconnu')
            d=["Maxime"]
            create_user(d)
            print(d)
            session["name_user"] = d[0]
            print(session)
            return redirect(url_for('homepage'))
        # return "Traitement de données" render_template("traitement.html")
    else:
        print(session)
        if "name_user" in session:
            return redirect(url_for('homepage'))
        return render_template("login.html")
    

@app.route('/logout')
def logout():
    print(session)
    session.pop("name_user", None)
    print(session)
    return redirect(url_for('login'))


@app.route('/logout_confirmation')
def logout_confirmation():
    return render_template("logout_confirmation.html")


@app.route('/formulaire')
def formulaire():
    return render_template("formulaire.html")






























@app.route("/heure")
def heure():
    date_heure = datetime.datetime.now()
    h = date_heure.hour
    m = date_heure.minute
    s = date_heure.second
    return render_template("heure.html", heure=h, minute=m, seconde=s)

# liste_eleves = [
#     {"nom" : 'Dupont', "prenom": 'Jean', "classe" : '2A'},
#     {"nom" : 'Dupont', "prenom": 'Jeanne', "classe" : 'TG2'},
#     {"nom" : 'Marchand', "prenom": 'Marie', "classe" : '2A'},
#     {"nom" : 'Martin', "prenom": 'Adeline', "classe" : '1G1'},
#     {"nom" : 'Dupont', "prenom": 'Lucas', "classe" : '2A'}
# ]

# @app.route("/eleves")
# def eleves():
#     classe = request.args.get('c')
#     if classe:
#         eleves_selectionnes = [eleve for eleve in liste_eleves if eleve ['classe'] == classe]    
#     else:
#         eleves_selectionnes = []
#     return render_template("eleves.html", eleves=eleves_selectionnes)

@app.route('/compteur')
def compteur():
    if "compteur" not in session:
        session ["compteur"] = 1
    else:
        session ["compteur"] += 1
    print(session)
    nb_visits = session ["compteur"]
    return f"Vous avez visité cette page {nb_visits} fois."

if __name__ =='__main__':
    app.run(debug=True)

    #https://www.youtube.com/watch?v=lvxqvNXniVc&list=PLV1TsfPiCx8PXHsHeJKvSSC8zfi4Kvcfs&index=2