from flask import Blueprint, render_template

errors_blueprint = Blueprint('errors', __name__, url_prefix='/errors')

@errors_blueprint.route('/<error_type>')
def error(error_type):
    return render_template(f'errors/{error_type}.html')