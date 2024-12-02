from flask import Flask, render_template
import datetime

app = Flask(__name__)

@app.route('/')
def welcome():
    return render_template("index.html")

@app.route("/heure")
def heure():
    date_heure = datetime.datetime.now()
    h = date_heure.hour
    m = date_heure.minute
    s = date_heure.second
    return render_template("heure.html", heure=h, minute=m, seconde=s)

liste_eleves = [
    {"nom" : 'Dupont', "prenom": 'Jean', "classe" : '2A'},
    {"nom" : 'Dupont', "prenom": 'Jeanne', "classe" : 'TG2'},
    {"nom" : 'Marchand', "prenom": 'Marie', "classe" : '2A'},
    {"nom" : 'Martin', "prenom": 'Adeline', "classe" : '1G1'},
    {"nom" : 'Dupont', "prenom": 'Lucas', "classe" : '2A'}
]

@app.route("/eleves")
def eleves():
    return render_template("eleves.html", eleves=liste_eleves)

if __name__ =='__main__':
    app.run(debug=True)

    #https://www.youtube.com/watch?v=lvxqvNXniVc&list=PLV1TsfPiCx8PXHsHeJKvSSC8zfi4Kvcfs&index=2