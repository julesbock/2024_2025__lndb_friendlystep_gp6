from flask import Blueprint, render_template, request
from datetime import date
from main_tools import *
import datetime, locale, platform

data_input_blueprint = Blueprint("data_input", __name__, url_prefix="/data_input")

@data_input_blueprint.route('/', methods=["POST", "GET"])

def data_input ():
    date_time = datetime.datetime.now()
    current_year = str(date_time.year)
    current_month = str(date_time.month)
    current_day = str(date_time.day)
    if platform.system() == "Windows":
        locale.setlocale(locale.LC_TIME, "French_France.1252")
    else:
        locale.setlocale(locale.LC_TIME, "fr_FR.UTF-8")
    today_date = date.today().strftime("%d %B %Y")

    all_user_data = load_data_from_user_file("user_data.json")

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
        return redirect(url_for('root.root'))
    else : 
        return render_template("user_data/data_input.html", today_date = today_date, data = existing_data)