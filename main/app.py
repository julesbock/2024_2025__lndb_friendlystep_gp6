from flask import Flask, render_templates, request

app = Flask (__name__)

@app.route ("/")


# fonction de lancement du programme
def initialize ():
    return render_templates (
        # insérer unre page html
    )

if __name__ == '__main__':
    app.run(debug=True)