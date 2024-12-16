from app import *
from data import *

def recherch_user(name_user, mdp):
    for user in users:
        if user["nom"] == name_user and user["mdp"] == mdp:
            return user
    return None