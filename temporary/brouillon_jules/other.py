import json, random
BASE32_ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ234567"
def generate_tournament_id():
    tournament_id = "".join(random.choices(BASE32_ALPHABET, k=11))
    return tournament_id

def check_if_tournament_id_exists(tournament_id, filename = "tournaments.json"):
    try:
        with open(filename, "r") as tournament_files:
            tournaments = json.load(tournament_files)
            return tournament_id in tournaments
    except (FileNotFoundError, json.JSONDecodeError):
        return False
    
def get_unique_tournament_id():
    while True:
        tournament_id = generate_tournament_id()
        if not check_if_tournament_id_exists(tournament_id):
            return tournament_id

def save_tournament_data(tournament_id, tournament_data):
    if not check_if_tournament_id_exists(tournament_id):
        with open(f"{tournament_id}.json", "r") as tournament_files:
            tournament_data = json.load(tournament_files)
    else:
         return False

print(get_unique_tournament_id())   