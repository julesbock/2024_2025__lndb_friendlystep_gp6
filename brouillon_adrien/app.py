from flask import Flask, render_template, request, redirect, url_for
# import datetime

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

# @app.route("/heure")
# def heure():
#     date_heure = datetime.datetime.now()
#     h = date_heure.hour
#     m = date_heure.minute
#     s = date_heure.second
#     return render_template("heure.html", heure=h, minute=m, seconde=s)

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
@app.route('/login')
def login():
    return render_template("login.html")

@app.route('/traitement', methods=["POST", "GET"])
def traitement():
    if request.method == "POST":
        # print(request.args)
        donnees = request.form
        nom = donnees.get('nom')
        mdp = donnees.get('mdp')
        if nom == 'admin' and mdp == "1234":
            return render_template("traitement.html", nom_utilisateur = nom)
        else:
            return render_template("traitement.html")
        # return "Traitement de données" render_template("traitement.html")
    else:
        return redirect(url_for('index'))
if __name__ =='__main__':
    app.run(debug=True)

    #https://www.youtube.com/watch?v=lvxqvNXniVc&list=PLV1TsfPiCx8PXHsHeJKvSSC8zfi4Kvcfs&index=2