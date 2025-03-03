from flask import Blueprint, render_template, request
from main_tools import do_all_graphics

user_data_graphics_blueprint = Blueprint("user_data_graphics", __name__, url_prefix="/user_data_graphics")

@user_data_graphics_blueprint.route('/<data_type>/<label_name>', methods=["POST", "GET"])
def user_data_graphics(data_type, label_name):
    if request.method == "GET":
        do_all_graphics(data_type, label_name)
        return render_template("user_data/user_data_graphics.html", label=label_name)
    else:
        return render_template("user_data/user_data_graphics.html", label=label_name)