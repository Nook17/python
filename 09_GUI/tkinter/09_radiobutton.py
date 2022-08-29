#!/usr/bin/env python3
# Python Tkinter GUI
# from - Bro Code
# https://www.youtube.com/watch?v=TuLxsvK4svQ&ab_channel=BroCode

from tkinter import *
from PIL import Image, ImageTk

food = ['pizza', 'burger', 'hotdog']


def order():
    if x.get() == 0:
        print("You ordered pizza")
    elif x.get() == 1:
        print("You ordered burger")
    elif x.get() == 2:
        print("You ordered hotdog")


# ----------- WINDOW -----------
root = Tk()
root.geometry('720x480')
root.title('Nook Window')
icon = PhotoImage(file='images/Logo_Nook_thin_radius_4.png')
root.iconphoto(True, icon)
root.config(background='#a0abbd')

# ----------- RESIZE IMAGE -----------
image = Image.open("images/pizza.png")
resize_image = image.resize((100,100))
pizzaImages = ImageTk.PhotoImage(resize_image)
image = Image.open("images/burger.png")
resize_image = image.resize((100,100))
burgerImages = ImageTk.PhotoImage(resize_image)
image = Image.open("images/hotdog.png")
resize_image = image.resize((100,100))
hotdogImages = ImageTk.PhotoImage(resize_image)

foodImages = [pizzaImages, burgerImages, hotdogImages]

x = IntVar()

# ----------- RADIOBUTTON -----------
for index in range(len(food)):
    radiobutton = Radiobutton(root,
                              text=food[index],
                              variable=x,
                              value=index,
                              padx=25,
                              font=('Impackt', 40),
                              image=foodImages[index],
                              compound='left',
                              indicatoron=False,
                              width=300,
                              command=order)

    # radiobutton.pack(anchor=W)
    radiobutton.pack()


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
