from flask import Blueprint, render_template
from main_tools import *

social_blueprint = Blueprint('social', __name__, url_prefix='/social')

@social_blueprint.route('/')
def social():
    return render_template('user_data/social.html')

@social_blueprint.route('/notifications')
def notifications():
    return render_template('user_data/notifications.html')

