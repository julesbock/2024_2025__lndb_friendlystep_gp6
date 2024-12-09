from flask import Flask, render_template, request, redirect, url_for, session
from data_brouillon.py import *
app = Flask(__name__)
app.secret_key = "039291df98be34655173c930564e88b1098ac6e1a173a61eacd268b6af8d7c44"

@app.route ("/")

# def helloword ():
#     return hellotext + maximetext

def bonjour ():
    return render_template ("formulaires.html")

@app.route('/submit', methods=['POST'])

def submit():
    # Récupérer les données du formulaire
    pas = request.form.get('pas')
    kilometres = request.form.get('kilometres')
    calories = request.form.get('calories')
    choix_du_sommeil = request.form.get('choix_du_sommeil')

    # Stocker les données dans un dictionnaire
    donnees = {
        "pas": int(pas) if pas else 0,
        "kilometres": float(kilometres) if kilometres else 0.0,
        "calories": int(calories) if calories else 0,
        "choix_du_sommeil": choix_du_sommeil
    }

    # Afficher ou utiliser le dictionnaire
    print("Données reçues :", donnees)

    # Retourner une réponse
    return f"Données enregistrées : {donnees}"

if __name__ == '__main__':
    app.run(debug=True)


@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method=="POST":
        donnees=request.form
        nom= donnees.get("nom")
        mdp= donnees.get("mdp")
        if nom =="Maxime" and mdp== "2468":
            return redirect(url_for('index'))
        else:
            return redirect(request.url)
    else:
        return render_template("login.html")



@app.route ("/compteur")
def compteur():
    if "compteur" not in session:
        session ["compteur"] = 1
    else:
        session["compteur"] = session["compteur"] + 1
    print(session)
    return "Nombre de visites"