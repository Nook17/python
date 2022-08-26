#!/usr/bin/env python3
# Python Tkinter GUI
# Program: calculator
# by Nook
from tkinter import *

expression = ''


def entry_text(item):
    global expression
    expression = expression + str(item)
    display_label.config(text=expression)


def equal_press():
    try:
        global expression
        total = str(eval(expression))
        display_label.config(text=total)
        expression = total
    except (Exception,):
        display_label.config(text="Error !!! - Try again")
        expression = ''


def clear_enter():
    global expression
    expression = ''
    display_label.config(text=expression)


def back_enter():
    global expression
    expression = expression[:-1]
    display_label.config(text=expression)


def sign_enter():
    global expression
    total = int(eval(expression)) * -1
    expression = str(total)
    display_label.config(text=expression)


# ----------- WINDOW -----------
root = Tk()
root.title('Calculator - Nook')
# root.geometry("400x400")
icon = PhotoImage(file='logo_Nook.png')
root.iconphoto(True, icon)
root.config(background='#152126')

# ----------- CLOCK -----------
display_label = Label(root, font=("Arial", 20), fg="#87c8b9", bg="#152126")
display_label.grid(row=1, column=1, columnspan=5)

one_button = Button(root, text='1', font=("Arial", 20), width=4, height=2, command=lambda: entry_text(1))
one_button.grid(row=5, column=1)
two_button = Button(root, text='2', font=("Arial", 20), width=4, height=2, command=lambda: entry_text(2))
two_button.grid(row=5, column=2)
three_button = Button(root, text='3', font=("Arial", 20), width=4, height=2, command=lambda: entry_text(3))
three_button.grid(row=5, column=3)
four_button = Button(root, text='4', font=("Arial", 20), width=4, height=2,  command=lambda: entry_text(4))
four_button.grid(row=4, column=1)
five_button = Button(root, text='5', font=("Arial", 20), width=4, height=2, command=lambda: entry_text(5))
five_button.grid(row=4, column=2)
six_button = Button(root, text='6', font=("Arial", 20), width=4, height=2, command=lambda: entry_text(6))
six_button.grid(row=4, column=3)
seven_button = Button(root, text='7', font=("Arial", 20), width=4, height=2, command=lambda: entry_text(7))
seven_button.grid(row=3, column=1)
eight_button = Button(root, text='8', font=("Arial", 20), width=4, height=2, command=lambda: entry_text(8))
eight_button.grid(row=3, column=2)
nine_button = Button(root, text='9', font=("Arial", 20), width=4, height=2, command=lambda: entry_text(9))
nine_button.grid(row=3, column=3)
zero_button = Button(root, text='0', font=("Arial", 20), width=10, height=2, command=lambda: entry_text(0))
zero_button.grid(row=6, column=1, columnspan=2)
dot_button = Button(root, text='.', font=("Arial", 20), width=4, height=2, command=lambda: entry_text('.'))
dot_button.grid(row=6, column=3)
percent_button = Button(root, text='%', font=("Arial", 20), width=4, height=2, command=lambda: entry_text('%'))
percent_button.grid(row=2, column=1)
divide_button = Button(root, text='/', font=("Arial", 20), width=4, height=2, command=lambda: entry_text('/'))
divide_button.grid(row=2, column=2)
times_button = Button(root, text='*', font=("Arial", 20), width=4, height=2, command=lambda: entry_text('*'))
times_button.grid(row=2, column=3)
minus_button = Button(root, text='-', font=("Arial", 20), width=4, height=2, command=lambda: entry_text('-'))
minus_button.grid(row=2, column=4)
plus_button = Button(root, text='+', font=("Arial", 20), width=4, height=4, command=lambda: entry_text('+'))
plus_button.grid(row=3, column=4, rowspan=2)
equal_button = Button(root, text='=', font=("Arial", 20), width=4, height=4, command=equal_press)
equal_button.grid(row=5, column=4, rowspan=2)
c_button = Button(root, text='C', font=("Arial", 20), width=4, height=2, command=back_enter)
c_button.grid(row=2, column=5)
ac_button = Button(root, text='AC', font=("Arial", 20), width=4, height=2, command=clear_enter)
ac_button.grid(row=3, column=5)
bracket_open_button = Button(root, text='(', font=("Arial", 20), width=4, height=2, command=lambda: entry_text('('))
bracket_open_button.grid(row=4, column=5)
bracket_close_button = Button(root, text=')', font=("Arial", 20), width=4, height=2,  command=lambda: entry_text(')'))
bracket_close_button.grid(row=5, column=5)
change_sign_button = Button(root, text='+/-', font=("Arial", 20), width=4, height=2, command=sign_enter)
change_sign_button.grid(row=6, column=5)

root.mainloop()
