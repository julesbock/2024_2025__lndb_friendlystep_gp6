from flask import Blueprint, render_template, request, redirect, url_for, session
from main_tools import * 

profil_blueprint = Blueprint("profil", __name__, url_prefix="/profil")

@profil_blueprint.route("/", methods=["POST", "GET"])
def profile():
    if request.method == "POST":
        user_personnal_data = {
            "first_name": request.form.get('first_name'),
            "last_name": request.form.get('last_name'),
            "username": request.form.get('username'),
            "mdp": request.form.get('mdp'),
            "email": request.form.get('email'),
            "birth_day": request.form.get('birth_day'),
            "birth_month": request.form.get('birth_month'),
            "birth_year": request.form.get('birth_year'),
            "gender_choice": request.form.get('gender_choice'),
            "nationality": request.form.get('nationality'),
            "height": request.form.get('height'),
            "weight": request.form.get('weight')
        }
        dump_data_in_user_file("personnal_data.json", user_personnal_data)
        return redirect(url_for('profil.profile'))
    else:
        user_personnal_data = load_data_from_user_file("personnal_data.json")
        return render_template("user_data/profil_settings.html", user=user_personnal_data)