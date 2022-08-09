#!/usr/bin/env python3
# Python Tkinter GUI
# from - Bro Code
# https://www.youtube.com/watch?v=TuLxsvK4svQ&ab_channel=BroCode

from tkinter import *

# ----------- WINDOW -----------
root = Tk()
root.geometry('720x480')
root.title('Nook Window')
icon = PhotoImage(file='images/Logo_Nook_thin_radius_4.png')
root.iconphoto(True, icon)
root.config(background='#a0abbd')


def submit():
    username = entry.get()
    print('Hello => {}'.format(username))


def delete():
    entry.delete(0, END)


def backspace():
    entry.delete(len(entry.get())-1, END)


# ----------- ENTRY -----------
entry = Entry(root,
              font=('Hack', 20),
              fg='blue',
              bg='#545c6b')
entry.pack(side=LEFT)
# entry.insert(0, 'placeholder')
# entry.config(show='*')
# entry.config(state=DISABLED)

submit_button = Button(root, text='send', command=submit)
submit_button.pack(side=RIGHT)

delete_button = Button(root, text='delete', command=delete)
delete_button.pack(side=RIGHT)

backspace_button = Button(root, text='backspace', command=backspace)
backspace_button.pack(side=RIGHT)



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
