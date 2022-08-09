#!/usr/bin/env python3
# Python Tkinter GUI
# from - Bro Code
# https://www.youtube.com/watch?v=TuLxsvK4svQ&ab_channel=BroCode

from tkinter import *
from PIL import Image, ImageTk

# ----------- WINDOW -----------
root = Tk()
root.geometry('720x480')
root.title('Nook Window')
icon = PhotoImage(file='images/Logo_Nook_thin_radius_4.png')
root.iconphoto(True, icon)
root.config(background='#a0abbd')

# ----------- RESIZE IMAGE -----------
image = Image.open("images/Python-Symbol.png")
resize_image = image.resize((150,100))
img = ImageTk.PhotoImage(resize_image)


def display():
    if x.get():
        print("You agree !")
    else:
        print("You don't agree :(")


# x = IntVar()
x = BooleanVar()
# x = StringVar()

# ----------- CHECKBUTTON -----------
check_button = Checkbutton(root,
                           text='I agree to something',
                           variable=x,
                           # onvalue=1,
                           # offvalue=0,
                           onvalue=True,
                           offvalue=False,
                           command=display,
                           font=('Arial', 20),
                           fg='#00FF00',
                           bg='black',
                           activeforeground='#00FF00',
                           activebackground='black',
                           padx=25,
                           pady=10,
                           image=img,
                           compound='bottom')
check_button.pack()


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
