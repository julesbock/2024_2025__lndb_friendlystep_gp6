from flask import Flask
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
from app_routes.errors_ap import *

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
app.register_blueprint(errors_blueprint)


# Présentation des routes enregistrées dans le terminal

print("Routes enregistrées :")
for rule in app.url_map.iter_rules():
    print(rule)

if __name__ =='__main__':
    app.run(debug=True, port = 5002)

