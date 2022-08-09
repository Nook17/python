#!/usr/bin/python3
from tkinter import *

window = Tk()

label1 = Label(window, text='Label_1', bg='red')
label2 = Label(window, text='Label_2', bg='yellow')
label3 = Label(window, text='Label_3', bg='purple')

label1.pack()
label2.pack(fill=X)
label3.pack(side=LEFT, fill=Y)

window.mainloop()