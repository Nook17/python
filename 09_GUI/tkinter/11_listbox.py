#!/usr/bin/env python3
# Python Tkinter GUI
# from - Bro Code
# https://www.youtube.com/watch?v=TuLxsvK4svQ&ab_channel=BroCode

from tkinter import *
# from PIL import Image, ImageTk


def submit():
    food = []
    # print(listbox.get(listbox.curselection()))
    for index in listbox.curselection():
        food.insert(index, listbox.get(index))
    print('You have ordered: ')
    for index in food:
        print(index)


def add():
    listbox.insert(listbox.size(), entryBox.get())
    listbox.config(height=listbox.size())


def delete():
    # listbox.delete(listbox.curselection())
    for index in reversed(listbox.curselection()):
        listbox.delete(index)
    listbox.config(height=listbox.size())


# ----------- WINDOW -----------
root = Tk()
# root.geometry('250x680')
root.title('Nook Window')
icon = PhotoImage(file='images/Logo_Nook_thin_radius_4.png')
root.iconphoto(True, icon)
root.config(background='#a0abbd')


# ----------- RESIZE IMAGE -----------
# image = Image.open("images/flame.png")
# resize_image = image.resize((130,110))
# flameImages = ImageTk.PhotoImage(resize_image)
# image = Image.open("images/ice.png")
# resize_image = image.resize((130,110))
# iceImages = ImageTk.PhotoImage(resize_image)


# ----------- LISTBOX -----------
listbox = Listbox(root,
                  bg='#f7ffde',
                  font=('Constantia', 35),
                  width=12,
                  selectmode=MULTIPLE)
listbox.pack()

listbox.insert(1, 'pizza')
listbox.insert(2, 'pasta')
listbox.insert(3, 'garlic bread')
listbox.insert(4, 'soup')
listbox.insert(5, 'salad')

listbox.config(height=listbox.size())

entryBox = Entry(root)
entryBox.pack()

submitButton = Button(root, text='submit', command=submit)
submitButton.pack()

addButton = Button(root, text='add', command=add)
addButton.pack()

deleteButton = Button(root, text='delete', command=delete)
deleteButton.pack()

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
