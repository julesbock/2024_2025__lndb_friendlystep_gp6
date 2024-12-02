#brouillon perso
from flask import Flask, render_templates, request

app = Flask (__name__)

@app.route ("/")
def bonjour():
    return render_templates ("formulaires.html")

if __name__ == '__main__':
    app.run(debug=True)