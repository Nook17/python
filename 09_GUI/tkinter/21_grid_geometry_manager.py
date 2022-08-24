#!/usr/bin/env python3
# Python Tkinter GUI
# from - Bro Code
# https://www.youtube.com/watch?v=TuLxsvK4svQ&ab_channel=BroCode

from tkinter import *


# ----------- WINDOW -----------
root = Tk()
root.title('Nook Window')
root.geometry("330x160")
icon = PhotoImage(file='images/Logo_Nook_thin_radius_4.png')
root.iconphoto(True, icon)
# root.config(background='#a0abbd')


# ----------- GRID GEOMETRY MANAGER -----------
titleLabel = Label(root, text='Enter your info', font=('Consolas', 25)).grid(row=0, column=0, columnspan=2)

firstnameLabel = Label(root, text='First name: ', width=20).grid(row=1, column=0)
firstNameEntry = Entry(root).grid(row=1, column=1)

lastnameLabel = Label(root, text='Last name: ', width=20).grid(row=2, column=0)
lastNameEntry = Entry(root).grid(row=2, column=1)

emailLabel = Label(root, text='email: ', width=20).grid(row=3, column=0)
emailEntry = Entry(root).grid(row=3, column=1)

button = Button(root, text='Submit').grid(row=4, column=0, columnspan=2)

root.mainloop()

# 06 ----------- WINDOW -----------
# 06 ----------- RESIZE IMAGE -----------
# 06 ----------- LABEL -----------
# 06 ----------- BUTTONS -----------
# 07 ----------- ENTRY -----------
# 08 ----------- CHECKBUTTON -----------
# 09 ----------- RADIOBUTTON -----------
# 10 ----------- SCALE -----------
# 11 ----------- LISTBOX -----------
# 12 ----------- MESSAGEBOX -----------
# 13 ----------- COLORCHOOSER -----------
# 14 ----------- TEXT AREA -----------
# 15 ----------- FILEDIALOG OPEN -----------
# 16 ----------- FILEDIALOG SAVE -----------
# 17 ----------- MENUBAR -----------
# 18 ----------- FRAMES -----------
# 19 ----------- OPEN NEW WINDOW -----------
# 20 ----------- WINDOW TABS -----------
# 21 ----------- GRID GEOMETRY MANAGER -----------
# 22 ----------- PROGRESSBAR -----------
# 23 ----------- CANVAS -----------
# 24 ----------- KEY EVENTS -----------
# 25 ----------- MOUSE EVENTS -----------
# 26 ----------- DRAG & DROP -----------
# 27 ----------- MOVE IMAGES -----------
# 28 ----------- ANIMATIONS -----------
# 29 ----------- MULTIPLE ANIMATIONS -----------
# 30 ----------- CLOCK PROGRAM -----------
