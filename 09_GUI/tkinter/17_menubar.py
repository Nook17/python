#!/usr/bin/env python3
# Python Tkinter GUI
# from - Bro Code
# https://www.youtube.com/watch?v=TuLxsvK4svQ&ab_channel=BroCode

from tkinter import *
from PIL import Image, ImageTk
# from tkinter import filedialog


def openFile():
    print('File has been opened!')


def saveFile():
    print('File has been saved!')


def cut():
    print('You cut some text')


def copy():
    print('You copied some text')


def paste():
    print('You pasted some text')


# ----------- WINDOW -----------
root = Tk()
root.title('Nook Window')
icon = PhotoImage(file='images/Logo_Nook_thin_radius_4.png')
root.iconphoto(True, icon)
root.config(background='#a0abbd')

# ----------- RESIZE IMAGE -----------
image = Image.open("images/open.png")
resize_image = image.resize((25, 25))
openImage = ImageTk.PhotoImage(resize_image)
image = Image.open("images/save.png")
resize_image = image.resize((25, 25))
saveImage = ImageTk.PhotoImage(resize_image)
image = Image.open("images/exit.png")
resize_image = image.resize((25, 25))
quitImage = ImageTk.PhotoImage(resize_image)
# openImage = PhotoImage(file='images/open.png')
# saveImage = PhotoImage(file='images/save.png')
# quitImage = PhotoImage(file='images/exit.png')

# ----------- MENUBAR -----------
menubar = Menu(root)
root.config(menu=menubar)

fileMenu = Menu(menubar, tearoff=0, font=('Arial', 13))
menubar.add_cascade(label='File', menu=fileMenu)
fileMenu.add_command(label='Open', command=openFile, image=openImage, compound='left')
fileMenu.add_command(label='Save', command=saveFile, image=saveImage, compound='left')
fileMenu.add_separator()
fileMenu.add_command(label='Quit', command=quit, image=quitImage, compound='left')

editMenu = Menu(menubar, tearoff=0, font=('Arial', 13))
menubar.add_cascade(label='Edit', menu=editMenu)
editMenu.add_command(label='Cut', command=cut)
editMenu.add_command(label='Copy', command=copy)
editMenu.add_command(label='Paste', command=paste)

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
