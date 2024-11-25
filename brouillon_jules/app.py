from flask import Flask

app = Flask(__name__)

hellotext = "<p>hello World!</p>"
maximetext = "<body>maxime sent le cochon fermenté</body>"

@app.route ("/")

def helloworld ():
    return hellotext + maximetext

if __name__ == '__main__':
    app.run(debug=True)

