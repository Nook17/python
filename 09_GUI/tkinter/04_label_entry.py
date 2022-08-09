#!/usr/bin/python3
from tkinter import *

root = Tk()
root.title("Nook root")
root.geometry("250x120")

label1 = Label(root, text='Name')
label2 = Label(root, text='Second name')
entry1 = Entry(root)
entry2 = Entry(root)

label1.grid(row=0, sticky=E)
label2.grid(row=1)

entry1.grid(row=0, column=1)
entry2.grid(row=1, column=1)

c = Checkbutton(root, text='Are you 18 years old?')
c.grid(columnspan=2)

root.mainloop()