#!/usr/bin/python3
from tkinter import *

root = Tk()
root.title("Nook root")
root.geometry("250x120")


def Nook(event):
    text = Text(root, height=2, width=15, bg='light yellow')
    text.insert(INSERT, 'Hello Nook')
    text.pack()


lab = Label(root, text='Beautiful Label')
lab.config(font=('Open Sans', 14))

button = Button(root, text='Click me')
button.bind('<Button-1>', Nook)

lab.pack()
button.pack()

root.mainloop()