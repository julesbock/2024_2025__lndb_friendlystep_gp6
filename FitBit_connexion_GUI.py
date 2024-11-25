import tkinter as tk
from tkinter import messagebox as mbox
import webbrowser
from fen_center import *
from data import *

class FitBitLoginApp:
    def __init__(self, root):
        self.root = root
        self.root.title(FitBit_fen_title)
        center_window(root, 500, 400)
        # self.root.attributes("-fullscreen", True)
        self.root.config(bg="white")

        # Titre
        tk.Label(
            root, text=FitBit_connexion_text, font=(Arial_police, 20, "bold"), bg="white"
        ).pack(pady=20)

        # Champ pour l'e-mail
        tk.Label(root, text=Mail_adress_text, font=(Arial_police, 12), bg="white").pack(pady=5)
        self.email_entry = tk.Entry(root, font=(Arial_police, 12), width=30, justify="center")
        self.email_entry.pack(pady=5)

        # Champ pour le mot de passe
        tk.Label(root, text=password_text, font=(Arial_police, 12), bg="white").pack(pady=5)
        self.password_entry = tk.Entry(root, font=(Arial_police, 12), width=30, show="*", justify="center")
        self.password_entry.pack(pady=5)

        # Bouton de connexion
        self.login_button = tk.Button(
            root, text=french_connexion_text, font=(Arial_police, 12, "bold"), bg="#4285F4", fg="white", 
            command=self.handle_login
        )
        self.login_button.pack(pady=20)

        # Message en bas
        self.create_account_label = tk.Label(
            root, text=account_creation_text, font=(Arial_police, 10), fg="blue", bg="white" , cursor="hand2"
        )
        self.create_account_label.pack(pady=10)
        self.create_account_label.bind("<Button-1>", self.create_account)

    def create_account(self, event):
        mbox.showinfo("Créer un compte", "Redirection vers la page de création de compte.")
        webbrowser.open(
            connexion_url
                )

    def handle_login(self):
        """Simule la connexion à FitBit."""
        email = self.email_entry.get()
        password = self.password_entry.get()

        # Exemple simple de validation
        if not email or not password:
            mbox.showwarning("Erreur", nothing_enter_text_error)
        elif "@" not in email:
            mbox.showwarning("Erreur", no_symbol_text_error)
        else:
            mbox.showinfo("Succès", f"Connexion réussie pour {email} (simulée).")

# Lancement de l'application
def connexion():
    root = tk.Tk()
    app = FitBitLoginApp(root)
    root.mainloop()