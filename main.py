from FitBit_connexion_GUI import *
import tkinter as tk
from fen_center import *
from data import *

class SimpleApp:
    def __init__(self, root):
        self.root = root
        self.root.title("")
        center_window(root, 200, 200)

        self.button = tk.Button(root, text=connexion_text, command=connexion)
        self.button.pack(pady=(80, 10))

# Main application
if __name__ == "__main__":
    root = tk.Tk()
    app = SimpleApp(root)
    root.mainloop()