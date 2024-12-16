from flask import Flask, render_template, request, redirect, url_for, session
import datetime

app = Flask(__name__)
app.secret_key = "02458d8b8e67adc5966be5f1b3e109341e2507abfd007fa2785cde99996611e5"
@app.route('/')
def homepage():
    return render_template("homepage.html")

users = [
    {"nom" : 'admin', "mdp":"1234"},
    {"nom" : 'marie', "mdp":"nsi"},
    {"nom" : 'paul', "mdp":"azerty"}
]


@app.route("/heure")
def heure():
    date_heure = datetime.datetime.now()
    h = date_heure.hour
    m = date_heure.minute
    s = date_heure.second
    return render_template("heure.html", heure=h, minute=m, seconde=s)

# liste_eleves = [
#     {"nom" : 'Dupont', "prenom": 'Jean', "classe" : '2A'},
#     {"nom" : 'Dupont', "prenom": 'Jeanne', "classe" : 'TG2'},
#     {"nom" : 'Marchand', "prenom": 'Marie', "classe" : '2A'},
#     {"nom" : 'Martin', "prenom": 'Adeline', "classe" : '1G1'},
#     {"nom" : 'Dupont', "prenom": 'Lucas', "classe" : '2A'}
# ]

# @app.route("/eleves")
# def eleves():
#     classe = request.args.get('c')
#     if classe:
#         eleves_selectionnes = [eleve for eleve in liste_eleves if eleve ['classe'] == classe]    
#     else:
#         eleves_selectionnes = []
#     return render_template("eleves.html", eleves=eleves_selectionnes)

def recherch_user(name_user, mdp):
    for user in users:
        if user["nom"] == name_user and user["mdp"] == mdp:
            return user
    return None

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
            return redirect(url_for('homepage'))
        else:
            print('utilisateur inconnu')
            return redirect(request.url)
        # return "Traitement de données" render_template("traitement.html")
    else:
        print(session)
        if "name_user" in session:
            return redirect(url_for('homepage'))
        return render_template("login.html")
    
@app.route('/logout')
def logout():
    print(session)
    session.pop("name_user", None)
    print(session)
    return redirect(url_for('login'))

@app.route('/logout_confirmation')
def logout_confirmation():
    return render_template("logout_confirmation.html")

@app.route('/formulaire')
def formulaire():
    return render_template("formulaire.html")

@app.route('/compteur')
def compteur():
    if "compteur" not in session:
        session ["compteur"] = 1
    else:
        session ["compteur"] += 1
    print(session)
    nb_visits = session ["compteur"]
    return f"Vous avez visité cette page {nb_visits} fois."

if __name__ =='__main__':
    app.run(debug=True)

    #https://www.youtube.com/watch?v=lvxqvNXniVc&list=PLV1TsfPiCx8PXHsHeJKvSSC8zfi4Kvcfs&index=2