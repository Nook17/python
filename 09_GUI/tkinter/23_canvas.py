#!/usr/bin/env python3
# Python Tkinter GUI
# from - Bro Code
# https://www.youtube.com/watch?v=TuLxsvK4svQ&ab_channel=BroCode

from tkinter import *


# ----------- WINDOW -----------
root = Tk()
root.title('Nook Window')
# root.geometry("330x160")
icon = PhotoImage(file='images/Logo_Nook_thin_radius_4.png')
root.iconphoto(True, icon)
# root.config(background='#a0abbd')


# ----------- CANVAS -----------
canvas = Canvas(root, height=500, width=500)
canvas.create_line(0, 0, 500, 500, fill='blue', width=5)
canvas.create_line(0, 500, 500, 0, fill='red', width=5)
canvas.create_rectangle(50, 50, 250, 250, fill='purple')
points = [250, 0, 500, 500, 0, 500]
canvas.create_polygon(points, fill='grey', outline='black', width=5)
canvas.create_arc(0, 0, 500, 500, style=PIESLICE, start=270, width=5)
# canvas.create_arc(0, 0, 500, 500, fill='red', extent=180, width=5)
# canvas.create_arc(0, 0, 500, 500, fill='white', extent=180, start=180, width=5)
# canvas.create_oval(190, 190, 310, 310, fill='white', width=5)
canvas.pack()

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
