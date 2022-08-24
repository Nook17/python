#!/usr/bin/env python3
# Python Tkinter GUI
# from - Bro Code
# https://www.youtube.com/watch?v=TuLxsvK4svQ&ab_channel=BroCode
import time
from tkinter import *
from PIL import Image, ImageTk

WIDTH = 500
HEIGHT = 500
xVelocity = 3
yVelocity = 2

# ----------- WINDOW -----------
root = Tk()
root.title('Nook Window')
# root.geometry("400x400")
icon = PhotoImage(file='images/Logo_Nook_thin_radius_4.png')
root.iconphoto(True, icon)
# root.config(background='#a0abbd')

# ----------- RESIZE IMAGE -----------
image = Image.open("images/Logo_Nook_thin_radius_4.png")
resize_image = image.resize((50, 50))
img = ImageTk.PhotoImage(resize_image)
background_photo = PhotoImage(file="images/Konrad_motocyklista.png")
# ----------- ANIMATIONS -----------
canvas = Canvas(root, width=WIDTH, height=HEIGHT)
canvas.pack()

background = canvas.create_image(0, 0, image=background_photo, anchor=NW)
my_image = canvas.create_image(0, 0, image=img, anchor=NW)

image_width = img.width()
image_height = img.height()

while True:
    coordinates = canvas.coords(my_image)
    if coordinates[0] >= WIDTH - image_width or coordinates[0] < 0:
        xVelocity = -xVelocity
    if coordinates[1] >= HEIGHT - image_height or coordinates[1] < 0:
        yVelocity = -yVelocity
    canvas.move(my_image, xVelocity, yVelocity)
    root.update()
    time.sleep(0.01)

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
