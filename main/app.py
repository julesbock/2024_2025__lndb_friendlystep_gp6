from flask import Flask, render_template, request, redirect, url_for, session
from tools import *
from data import *

app = Flask(__name__)

app.secret_key = "02458d8b8e67adc5966be5f1b3e109341e2507abfd007fa2785cde99996611e5"


@app.route('/')
def root():
    return render_template("root.html")

@app.route('/login',  methods=["POST", "GET"])
def login():
    if request.method == "POST":
        # print(request.args)
        donnees = request.form
        nom = donnees.get('nom')
        mdp = donnees.get('mdp')
        user=recherch_user(nom, mdp)
        if user is not None:
            print('utilisateur trouvé')
            session["name_user"] = user['nom']
            print(session)
            return redirect(url_for('root'))
        else:
            print('utilisateur inconnu')
            return redirect(request.url)
        # return "Traitement de données" render_template("traitement.html")
    else:
        print(session)
        if "name_user" in session:
            return redirect(url_for('root'))
        return render_template("login.html")
    
@app.route('/logout')
def logout():
    print(session)
    session.pop("name_user", None)
    print(session)
    return redirect(url_for('root'))

@app.route('/logout_confirmation')
def logout_confirmation():
    return render_template("logout_confirmation.html")

@app.route('/forms')
def forms():
    return render_template("forms.html")

@app.route ('/sign_up')
def sign_up ():
    return render_template ("sign_up.html")

@app.route ('/import')
def data_import ():
    return render_template ("data_import.html")

if __name__ =='__main__':
    app.run(debug=True)
