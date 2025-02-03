from flask import Blueprint, render_template

faq_blueprint = Blueprint("faq", __name__, url_prefix="/faq")

@faq_blueprint.route("/")
def faq():
    return render_template("faq.html")