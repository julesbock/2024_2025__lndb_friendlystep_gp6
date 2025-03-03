import os
import json

# Chemin vers le dossier contenant les fichiers de tournois
tournaments_dir = os.path.join(os.path.dirname(__file__), 'data', 'tournaments_data', 'tournaments')

# Chemin vers le fichier où vous souhaitez sauvegarder les joueurs
players_file_path = os.path.join(os.path.dirname(__file__), 'data', 'tournaments_data', 'tournaments_players.json')

# Dictionnaire pour stocker les tournois et les joueurs
tournaments_players_data = {}

# Parcours de tous les fichiers JSON dans le dossier tournaments
for filename in os.listdir(tournaments_dir):
    if filename.endswith('.json'):
        # Récupération de l'ID du tournoi depuis le nom du fichier (supposé être le nom du fichier)
        tournament_id = filename.replace('.json', '')
        
        # Ajout de l'ID du tournoi dans le dictionnaire avec une liste vide pour les joueurs
        tournaments_players_data[tournament_id] = ["hduu"]

    

# Sauvegarde du dictionnaire dans le fichier JSON
with open(players_file_path, 'w') as players_file:
    json.dump(tournaments_players_data, players_file, indent=4)

print("Données des joueurs sauvegardées avec succès dans 'tournaments_players.json'")