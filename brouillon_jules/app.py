from flask import Flask, render_template, request
app = Flask(__name__)



@app.route ("/")


def home ():
    return render_template ("home.html")

@app.route('/submit', methods=['POST'])

@app.route ('/account_settings')

def account_settings ():
    return render_template("account_settings.html")

@app.route ('/login')
def login ():
    return render_template ("login.html")


if __name__ == '__main__':
    app.run(debug=True)

