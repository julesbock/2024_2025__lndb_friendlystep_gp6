from flask import Flask, jsonify
from main_tools import *
from app_routes.root_ap import *
from app_routes.sign_up_ap import *
from app_routes.profile_ap import * 
from app_routes.data_input_ap import *
from app_routes.login_ap import *
from app_routes.logout_ap import *
from app_routes.tournament_ap import *
from app_routes.faq_ap import *
from app_routes.user_data_graphics_ap import *
import openai 

app = Flask(__name__)

app.secret_key = "02458d8b8e67hbd5966be5f1b3e109341e2507abfd007fa2785cde99996611e5"



# Enregistrement des routes dans l'application

app.register_blueprint(root_blueprint) 
app.register_blueprint(login_blueprint)
app.register_blueprint(logout_blueprint)
app.register_blueprint(sign_up_blueprint)
app.register_blueprint(profil_blueprint)
app.register_blueprint(data_input_blueprint)
app.register_blueprint(tournaments_blueprint)
app.register_blueprint(faq_blueprint)
app.register_blueprint(user_data_graphics_blueprint)

# Présentation des routes enregistrées dans le terminal
openai.api_base = "http://localhost:11434/v1"  # Utilisation de l'API locale d'Ollama
openai.api_key = "ollama"  # Une clé est requise, mais n'importe quelle valeur fonctionne
print("Routes enregistrées :")
for rule in app.url_map.iter_rules():
    print(rule)
    
# Route to render the chatbot interface
@app.route('/chatbot')
def chatbot_page():
    return render_template("chatbot.html")

# Route for handling chatbot API requests (JSON)
@app.route('/chatbot/api', methods=['POST'])
def chatbot_api():
    user_input = request.json.get("message", "")
    text = "Voici les informations à connaitre pour répondre aux questions: "
    text += "- Pour créer un compte, aller sur www.toto.com/creer_compte\n"
    text += "- Pour inviter un utilisateur, aller sur www.toto.com/inviter_utilisateur\n"
    text += "Si tu n'as pas de réponse, indiques d'abord que tu n'as pas de réponse, puis fais une synthèse des sujets auxquels tu sais répondre.\n"
    text += "Voici la question de l'utilisateur: "
    text += str(user_input)
    response = chatbot_response(text)  # Replace with actual logic
    return jsonify({"response": response})

def chatbot_response(user_input):
    try:
        # Appel à l'API OpenAI pour obtenir une réponse
        response = openai.Completion.create(
            model="mistral",  # Nom du modèle d'Ollama téléchargé
            prompt=user_input,  # Utilisation de l'input utilisateur comme prompt
            max_tokens=150,
            temperature=0.7
        )
        message = response.choices[0].text.strip()  # Extrait le texte de la réponse
        return message
    except Exception as e:
        return f"Erreur dans l'API OpenAI: {e}"
    
if __name__ =='__main__':
    app.run(debug=True, port=5010)
