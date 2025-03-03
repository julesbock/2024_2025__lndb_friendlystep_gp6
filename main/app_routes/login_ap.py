from flask import render_template, request, redirect, url_for, Blueprint, session
from main_tools import *

login_blueprint = Blueprint("login", __name__, url_prefix="/login")

@login_blueprint.route("/", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        donnees = request.form
        nom = donnees.get('nom')
        mdp = donnees.get('mdp')
        user = recherch_user(nom, mdp)
        if user is not None:
            session["name_user"] = user['username']
            return redirect(url_for('root.root'))
        else:
            print('utilisateur inconnu')
            return render_template("users/login.html", error = "Utilisateur ou mot de passe inconnu. Veuillez réessayer.")
    else:
        if "name_user" in session:
            return redirect(url_for('root.root'))
        return render_template("users/login.html")