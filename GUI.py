from tkinter import * 


def create_GUI (): 
    gui = GUI ()
    gui.open_fen()
    show_classed_data ()

class GUI () :

    def __init__(self):
        self.fen = Tk()
        self.fen.geometry("300x300")
        self.fen.attributes("-fullscreen", True)
        self.fen.bind("<Escape>", lambda e: self.fen.destroy())

    def open_fen (self):
        self.fen.mainloop()

def show_classed_data ():
    print(" Hi")

