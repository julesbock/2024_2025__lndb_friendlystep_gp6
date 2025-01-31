from flask import Flask, render_template, request, redirect, url_for, session
from datetime import date
from tools import *
from app_routes.sign_up_ap import *
from app_routes.login_ap import *
from app_routes.logout_ap import *
from app_routes.tournament_ap import *
import os, datetime, json, locale, platform

app = Flask(__name__)

app.secret_key = "02458d8b8e67hbd5966be5f1b3e109341e2507abfd007fa2785cde99996611e5"


@app.route('/')
def root():
    if "name_user" in session:
        all_user_data = get_data("user_data.json")
        existing_data = check_if_data_exists (all_user_data)
        return render_template("root.html", data=existing_data, is_logged = True)
    else:
        return render_template('root.html', data=None, is_logged = False)
    
@app.route('/user_data_graphics/<data_type>/<label_name>', methods=["POST", "GET"])
def user_data_graphics(data_type, label_name):

    if request.method == "GET":
        do_all_graphics(data_type, label_name)
        return render_template("user_data_graphics.html", label=label_name)
    else:
        return render_template("user_data_graphics.html", label=label_name)
    

@app.route('/data_input', methods=["POST", "GET"])
def data_input ():
    date_time = datetime.datetime.now()
    current_year = str(date_time.year)
    current_month = str(date_time.month)
    current_day = str(date_time.day)
    if platform.system() == "window":
        locale.setlocale(locale.LC_TIME, "French_France")
    else:
        locale.setlocale(locale.LC_TIME, "fr_FR.UTF-8")
    today_date = date.today().strftime("%d %B %Y")

    all_user_data = get_data("user_data.json")

    existing_data = check_if_data_exists (all_user_data)
    
    if request.method == "POST" :
        personnal_data = {
            "step_data" : request.form['step_data'],
            "distance_data" : request.form['distance_data'],
            "calories_data" : request.form['calories_data'],
            "floors_data" : request.form['floors_data'],
            "sleep_duration_data" : request.form['sleep_duration_data'],
            "sleep_score_data" : request.form['sleep_score_data']
        }
        put_data_in_user_data( personnal_data)
        return redirect(url_for('root'))
    else : 
        return render_template("data_input.html", today_date = today_date, data = existing_data)
    
@app.route("/profil", methods=["POST", "GET"])
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
        give_data("personnal_data.json", user_personnal_data)
        return redirect(url_for('profile'))
    else:
        user_personnal_data = get_data("personnal_data.json")
        return render_template("profil_settings.html", user=user_personnal_data)

app.register_blueprint(login_blueprint)
app.register_blueprint(logout_blueprint)

app.register_blueprint(sign_up_blueprint)  
app.register_blueprint(tournaments_blueprint)

@app.route("/faq")
def faq():
    return render_template("faq.html")


# Présentation des routes enregistrées dans le terminal

print("Routes enregistrées :")
for rule in app.url_map.iter_rules():
    print(rule)

if __name__ =='__main__':
    app.run(debug=True)

