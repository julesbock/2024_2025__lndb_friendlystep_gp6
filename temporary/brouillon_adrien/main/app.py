from flask import Flask, render_template, request, redirect, url_for, session
from tools import *
from data import *
import os, datetime, json

app = Flask(__name__)

app.secret_key = "02458d8b8e67adc5966be5f1b3e109341e2507abfd007fa2785cde99996611e5"


@app.route('/')
def root():
    return render_template("root.html")

@app.route('/login',  methods=["POST", "GET"])
def login():
    if request.method == "POST":
        donnees = request.form
        nom = donnees.get('nom')
        mdp = donnees.get('mdp')
        user = recherch_user(nom, mdp)
        if user is not None:
            print('utilisateur trouvé')
            session["name_user"] = user['username']
            print(session)
            return redirect(url_for('root'))
        else:
            print('utilisateur inconnu')
            return render_template("login.html", error = "Utilisateur ou mot de passe inconnu. Veuillez réessayer.")
    else:
        print(session)
        if "name_user" in session:
            return redirect(url_for('root'))
        return render_template("login.html")
    
@app.route('/logout')
def logout():
    print(session)
    session.pop("name_user", None)
    print(session)
    return redirect(url_for('root'))

@app.route('/logout_confirmation')
def logout_confirmation():
    return render_template("logout_confirmation.html")

def put_data(personnal_user_data): 
    dossier_projet = os.path.dirname(__file__)
    chemin_user = os.path.join(dossier_projet, "users", session["name_user"])
    chemin_file = os.path.join(chemin_user, "user_data.json")
    with open(chemin_file, "r") as json_file:
        all_data = json.load(json_file)
    date_heure = datetime.datetime.now()
    current_year = str(date_heure.year)
    current_month = str(date_heure.month)
    current_day = str(date_heure.day)


    # if "user_data" not in all_data:
    #     all_data["user_data"] = {}
    # if current_year not in all_data["user_data"]:
    #     all_data["user_data"][current_year] = {}
    # if current_month not in all_data["user_data"][current_year]:
    #     all_data["user_data"][current_year][current_month] = {}
    # if current_day not in all_data["user_data"][current_year][current_month]:
    #     all_data["user_data"][current_year][current_month][current_day] = []

    all_data = check_if_all_good(all_data, current_year, current_month, current_day)
    all_data ["user_data"][current_year][current_month][current_day] = (personnal_user_data)
    with open(chemin_file, "w") as json_file:
        json.dump(all_data, json_file, indent=4)

def check_if_all_good(dic, current_year, current_month, current_day):
    dic.setdefault('user_data', {}).setdefault(current_year, {}).setdefault(current_month, {}).setdefault(current_day, {})
    return dic

@app.route('/data_input', methods=["POST", "GET"])
def data_input ():
    if request.method == "POST" :
        personnal_data = {
            "donnees_pas" : request.form['step_data'],
            "kilometres parcourus" : request.form['kilomètres'],
            "calories" : request.form['calories'],
            "sleep_quality" : request.form['sleep_quality']
        }
        # ne pas mettre d accent sinon cela va les coder ex : \u00e9 pour "é"

        put_data(personnal_data)
    return render_template("data_input.html")


@app.route ('/import')
def data_import ():
    return render_template ("data_import.html")
    
@app.route('/sign_up', methods=["POST", "GET"])
def sign_up():
    if request.method == "POST":
        user_dico = {
            "first_name" : request.form['first_name'],
            "last_name" : request.form['last_name'],
            "username" : request.form['username'],
            "mdp" : request.form['mdp'],
            "email" : request.form['email'],
            "birth_day" : request.form['birth_day'],
            "birth_month" : request.form['birth_month'],
            "birth_year" : request.form['birth_year'],
            "gender_choice" : request.form['gender_choice'],
            "nationality" : request.form['nationality'],
            "height" : request.form['height'],
            "weight" : request.form['weight']
        }
        create_and_register_user(user_dico)
        session["name_user"] = user_dico['username']

        return redirect(url_for('root'))
    
    return render_template("sign_up.html")

@app.route('/dashboard')
def dashboard():
    # Obtenir la date actuelle
    date_heure = datetime.datetime.now()
    current_year = date_heure.year
    current_month = date_heure.month
    current_day = date_heure.day

    # Récupérer les données de l'utilisateur pour aujourd'hui, les 7 derniers jours, le mois, et l'année
    user_data = get_user_data()

    # Données pour le jour même
    today_data = user_data["user_data"][str(current_year)][str(current_month)].get(str(current_day), {})

    # Données pour les 7 derniers jours
    last_7_days_data = get_last_7_days_data(user_data, current_year, current_month, current_day)

    # Données pour le mois actuel
    month_data = get_month_data(user_data, current_year, current_month, current_day)

    # Données pour l'année actuelle
    year_data = get_year_data(user_data, current_year, current_month)

    # Passer les données au template
    return render_template("dashboard.html", 
                           today_data=today_data, 
                           last_7_days_data=last_7_days_data, 
                           month_data=month_data,
                           year_data=year_data)
def get_user_data():
    # Récupérer les données de l'utilisateur à partir du fichier JSON
    dossier_projet = os.path.dirname(__file__)
    chemin_user = os.path.join(dossier_projet, "users", session["name_user"], "user_data.json")
    with open(chemin_user, "r") as json_file:
        all_data = json.load(json_file)
    return all_data

def get_last_7_days_data(user_data, current_year, current_month, current_day):
    # Récupérer les données des 7 derniers jours
    last_7_days = []
    for i in range(7):
        day = current_day - i
        if day <= 0:
            current_month -= 1
            if current_month <= 0:
                current_year -= 1
                current_month = 12
            day = calendar.monthrange(current_year, current_month)[1] + day
        last_7_days.append(user_data["user_data"][str(current_year)][str(current_month)].get(str(day), {}))
    return last_7_days

def get_month_data(user_data, current_year, current_month, current_day):
    # Récupérer les données du mois actuel
    month_data = {}
    for day in range(1, current_day + 1):
        month_data[day] = user_data["user_data"][str(current_year)][str(current_month)].get(str(day), {})
    return month_data

def get_year_data(user_data, current_year, current_month):
    # Récupérer les données de l'année actuelle
    year_data = {}
    for month in range(1, current_month + 1):
        year_data[month] = user_data["user_data"][str(current_year)].get(str(month), {})
    return year_data

if __name__ =='__main__':
    app.run(debug=True)