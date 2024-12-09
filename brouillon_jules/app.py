from flask import Flask, render_template, request

app = Flask(__name__)

hellotext = "<p>hello World!</p>"
maximetext = "<body>maxime sent le cochon fermenté</body>"

@app.route ("/")

# def helloword ():
#     return hellotext + maximetext

def bonjour ():
    return render_template ("test_template_chatgpt.html")

@app.route('/submit', methods=['POST'])

@app.route ('/login')

def login ():
    return render_template("login.html")

# def submit():
    # Récupérer les données du formulaire
    pas = request.form.get('pas')
    kilometres = request.form.get('kilometres')
    calories = request.form.get('calories')
    choix_du_sommeil = request.form.get('choix_du_sommeil')

    # Stocker les données dans un dictionnaire
    donnees = {
        "pas": int(pas) if pas else 0,
        "kilometres": float(kilometres) if kilometres else 0.0,
        "calories": int(calories) if calories else 0,
        "choix_du_sommeil": choix_du_sommeil
    }

    # Afficher ou utiliser le dictionnaire
    print("Données reçues :", donnees)

    # Retourner une réponse
    return f"Données enregistrées : {donnees}"

if __name__ == '__main__':
    app.run(debug=True)

