from flask import Flask, render_template, request

app = Flask(__name__)

hellotext = "<p>hello World!</p>"
maximetext = "<body>maxime sent le cochon fermenté</body>"

@app.route ("/")

# def helloword ():
#     return hellotext + maximetext

def bonjour ():
    return render_template ("test_template_chatgpt.html")



if __name__ == '__main__':
    app.run(debug=True)

