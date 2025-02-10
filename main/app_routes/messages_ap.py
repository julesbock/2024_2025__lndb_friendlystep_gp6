from flask import Blueprint, render_template

messages_blueprint = Blueprint('messages', __name__, url_prefix='/messages')

@messages_blueprint.route('/')
def messages():
    return render_template('user_data/messages.html')