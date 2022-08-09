#!/usr/bin/env python3
# Python Tkinter GUI
# from - Bro Code
# https://www.youtube.com/watch?v=TuLxsvK4svQ&ab_channel=BroCode

from tkinter import *
from tkinter import messagebox
# from PIL import Image, ImageTk


def click():
    # messagebox.showinfo(title='This is an message box', message='You are a person')

    # if messagebox.askokcancel(title='ask ok or cancel',
    #                           message='Do you want to do the thing ?'):
    #     print('You did a thing!')
    # else:
    #     print('You canceled a thing :(')

    # answer = messagebox.askquestion(title='ask question', message='Do you like me?')
    # if answer == 'yes':
    #     print('I like you too')
    # else:
    #     print("Why you don't like me")

    answer = messagebox.askyesnocancel(title='ask question', message='Do you like me?', icon='info')
    if answer:
        print('I like you too')
    elif answer == False:
        print("Why you don't like me")
    else:
        print('Good by')


# ----------- WINDOW -----------
root = Tk()
root.geometry('300x200')
root.title('Nook Window')
icon = PhotoImage(file='images/Logo_Nook_thin_radius_4.png')
root.iconphoto(True, icon)
root.config(background='#a0abbd')


# ----------- RESIZE IMAGE -----------
# image = Image.open("images/flame.png")
# resize_image = image.resize((130,110))
# flameImages = ImageTk.PhotoImage(resize_image)

# ----------- MESSAGEBOX -----------
button = Button(root, text='click me', command=click)
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
