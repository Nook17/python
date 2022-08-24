#!/usr/bin/env python3
# Python Tkinter GUI
# from - Bro Code
# https://www.youtube.com/watch?v=TuLxsvK4svQ&ab_channel=BroCode

from tkinter import *
from PIL import Image, ImageTk


def move_up(event):
    canvas.move(myimage, 0, -5)


def move_down(event):
    canvas.move(myimage, 0, 5)


def move_left(event):
    canvas.move(myimage, -5, 0)


def move_right(event):
    canvas.move(myimage, 5, 0)

# ----------- WINDOW -----------
root = Tk()
root.title('Nook Window')
# root.geometry("400x400")
icon = PhotoImage(file='images/Logo_Nook_thin_radius_4.png')
root.iconphoto(True, icon)
# root.config(background='#a0abbd')

# ----------- RESIZE IMAGE -----------
image = Image.open("images/Logo_Nook_thin_radius_4.png")
resize_image = image.resize((150, 150))
img = ImageTk.PhotoImage(resize_image)

# ----------- MOVE IMAGES CANVAS -----------
canvas = Canvas(root, width=500, height=500)
canvas.pack()

myimage = canvas.create_image(0, 0, image=img, anchor=NW)

root.bind("<w>", move_up)
root.bind("<s>", move_down)
root.bind("<a>", move_left)
root.bind("<d>", move_right)
root.bind("<Up>", move_up)
root.bind("<Down>", move_down)
root.bind("<Left>", move_left)
root.bind("<Right>", move_right)

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
