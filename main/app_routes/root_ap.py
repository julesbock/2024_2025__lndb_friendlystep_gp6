from flask import Blueprint, render_template, session
from main_tools import *

root_blueprint = Blueprint("root", __name__, url_prefix="/")

@root_blueprint.route("/")
def root():
    if "name_user" in session:
        all_user_data = load_data_from_user_file("user_data.json")
        existing_data = check_if_data_exists (all_user_data)
        return render_template("root.html", data=existing_data, is_logged = True)
    else:
        return render_template('root.html', data=None, is_logged = False)