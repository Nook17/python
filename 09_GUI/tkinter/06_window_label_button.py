#!/usr/bin/env python3
# Python Tkinter GUI
# from - Bro Code
# https://www.youtube.com/watch?v=TuLxsvK4svQ&ab_channel=BroCode

from tkinter import *
from PIL import Image, ImageTk

# ----------- WINDOW -----------
root = Tk()
root.geometry('420x420')
root.title('Nook Window')
icon = PhotoImage(file='images/Logo_Nook_thin_radius_4.png')
root.iconphoto(True, icon)
root.config(background='#151116')

# ----------- RESIZE IMAGE -----------
image = Image.open("images/ASzWoj_logo.png")
resize_image = image.resize((150, 150))
img = ImageTk.PhotoImage(resize_image)

# ----------- LABEL -----------
label = Label(root,
              text='Hello Nook',
              font=('Hack', 20, 'bold'),
              fg='#32876e',
              bg='#152126',
              relief=RAISED,
              bd=10,
              padx=20,
              pady=20,
              image=img,
              compound='top')

label.pack()
# label.place(x=200, y=200)

# ----------- BUTTONS -----------
count = 0


def click():
    global count
    count += 1
    print(count)


image2 = Image.open("images/thumb_up.png")
resize_image2 = image2.resize((50, 50))
thumbUp = ImageTk.PhotoImage(resize_image2)

button = Button(root,
                text='click me!',
                command=click,
                font=('Terminus', 25, 'bold'),
                fg='#152126',
                bg='green',
                activeforeground='#152126',
                activebackground='green',
                state=ACTIVE,
                image=thumbUp,
                compound='top')

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
