#!/usr/bin/env python3
# Python Tkinter GUI
# from - Bro Code
# https://www.youtube.com/watch?v=TuLxsvK4svQ&ab_channel=BroCode

from tkinter import *
from PIL import Image, ImageTk

def submit():
    print('The temperature is: {}'.format(scale.get()))


# ----------- WINDOW -----------
root = Tk()
# root.geometry('250x680')
root.title('Nook Window')
icon = PhotoImage(file='images/Logo_Nook_thin_radius_4.png')
root.iconphoto(True, icon)
root.config(background='#a0abbd')


# ----------- RESIZE IMAGE -----------
image = Image.open("images/flame.png")
resize_image = image.resize((130,110))
flameImages = ImageTk.PhotoImage(resize_image)
image = Image.open("images/ice.png")
resize_image = image.resize((130,110))
iceImages = ImageTk.PhotoImage(resize_image)


# ----------- SCALE -----------
hotLabel = Label(image=flameImages)
hotLabel.pack()

scale = Scale(root,
              from_=100,
              to=0,
              length=600,
              orient=VERTICAL,
              font=('Consolas', 20),
              tickinterval=10,
              # showvalue=False,
              resolution=5,
              troughcolor='#a0abbd',
              fg='black',
              bg='grey')
# scale.set(17)
# scale.set(((scale['from'] - scale['to']) / 2) + scale['to'])
scale.pack()

iceLabel = Label(image=iceImages)
iceLabel.pack()

button = Button(root,
                text='submit',
                command=submit)
button.pack()

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
