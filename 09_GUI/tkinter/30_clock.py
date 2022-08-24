#!/usr/bin/env python3
# Python Tkinter GUI
# from - Bro Code
# https://www.youtube.com/watch?v=TuLxsvK4svQ&ab_channel=BroCode
from time import *
from tkinter import *


def update():
    time_string = strftime("%H:%M:%S")
    date_string = strftime("%A - %d %B %Y")
    time_label.config(text=time_string)
    date_label.config(text=date_string)

    time_label.after(1000, update)


# ----------- WINDOW -----------
root = Tk()
root.title('Nook Window')
# root.geometry("400x400")
icon = PhotoImage(file='images/Logo_Nook_thin_radius_4.png')
root.iconphoto(True, icon)
root.config(background='#152126')

# ----------- CLOCK -----------
time_label = Label(root, font=("Arial",50), fg="#87c8b9", bg="#152126")
time_label.pack()

date_label = Label(root, font=("Arial",20), fg="#32876e", bg="#152126")
date_label.pack()

update()

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
# '<font color="#87c8b9">'dddd'</font>',  d MMM, '<font color="#0cb8e8"><b>'HH:mm:s'</b></font>'
