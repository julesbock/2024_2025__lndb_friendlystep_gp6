from flask import render_template, request, redirect, url_for, Blueprint, session

logout_blueprint = Blueprint('logout', __name__, url_prefix='/logout')

@logout_blueprint.route('/')
def logout():
    print(session)
    session.pop("name_user", None)
    print(session)
    return redirect(url_for('root.root'))

@logout_blueprint.route('/logout_confirmation')
def logout_confirmation():
    return render_template("users/logout_confirmation.html")
