from app import *
def login():
    if request.method == "POST":
        donnees = request.form
        nom = donnees.get('nom')
        mdp = donnees.get('mdp')
        user = recherch_user(nom, mdp)
        if user is not None:
            print('utilisateur trouvé')
            session["name_user"] = user['username']
            print(session)
            return redirect(url_for('root'))
        else:
            print('utilisateur inconnu')
            return render_template("login.html", error = "Utilisateur ou mot de passe inconnu. Veuillez réessayer.")
    else:
        print(session)
        if "name_user" in session:
            return redirect(url_for('root'))
        return render_template("login.html")