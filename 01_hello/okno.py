#!/usr/bin/python3


from tkinter import *

class Application(Frame):
    """ Aplikacja z GUI Okienko Koja """
    def __init__(self, master):
        super(Application, self).__init__(master) 
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        """ Kojo tu pisz """
        # utwórz etykietę z opisem
        Label(self,
              text = "Konrad tu możesz pisać swój tekst"
              ).grid(row = 0, column = 0, sticky = W)

        # utwórz pole tekstowe
        self.results_txt = Text(self, width = 100, height = 20, wrap = WORD)
        self.results_txt.grid(row = 20, column = 0, columnspan = 3)

# część główna
root = Tk()
root.title("Okno koja")
root.geometry("740x350")
app = Application(root)
root.mainloop()
