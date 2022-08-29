#!/usr/bin/env python3
# -------------------------------------
# Python Tkinter GUI
# Program: calculator
# Version: 1.1
# start project: 26 August 2022 r.
# by Nook
# -------------------------------------
import tkinter
from tkinter import *

expression = ''
B_WIDTH = 70         # 4 2 10 4
B_HEIGHT = 70
B_WIDTH_RECT = 8
B_HEIGHT_RECT = 4
B_X = 10
B_Y = 80
B_PADDING = 80
BG_COLOR = "#152126"
FG_COLOR = "#87c8b9"
BG_COLOR_ACTIVE = '#1b2b31'
FG_COLOR_ACTIVE = '#32876e'


def entry_text(item):
    global expression
    expression = expression + str(item)
    display_label.config(text=expression)


def entry_text_key(event):
    global expression
    expression = expression + event.keysym
    display_label.config(text=expression)


def equal_press():
    try:
        global expression
        total = str(eval(expression))
        display_label.config(text=total)
        terminal2.insert(END, "{} = {}\n".format(expression, total))
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
root.geometry("430x605")
icon = PhotoImage(file='logo_Nook.png')
root.iconphoto(True, icon)
root.config(background=BG_COLOR)
root.resizable(False, False)

# ----------- CLOCK -----------
# root.bind("<Key>", entry_text_key)
root.bind("1", lambda event: entry_text(1))
root.bind("2", lambda event: entry_text(2))
root.bind("3", lambda event: entry_text(3))
root.bind("4", lambda event: entry_text(4))
root.bind("5", lambda event: entry_text(5))
root.bind("6", lambda event: entry_text(6))
root.bind("7", lambda event: entry_text(7))
root.bind("8", lambda event: entry_text(8))
root.bind("9", lambda event: entry_text(9))
root.bind("0", lambda event: entry_text(10))
root.bind("-", lambda event: entry_text('-'))
root.bind("+", lambda event: entry_text('+'))
root.bind("*", lambda event: entry_text('*'))
root.bind("/", lambda event: entry_text('/'))
root.bind("(", lambda event: entry_text('('))
root.bind(")", lambda event: entry_text(')'))
root.bind(".", lambda event: entry_text('.'))
root.bind("<Return>", lambda event: equal_press())
root.bind("<Escape>", lambda event: clear_enter())
root.bind("<BackSpace>", lambda event: back_enter())

# display_label = Label(root, font=("Arial", 20), fg=FG_COLOR, bg=BG_COLOR_ACTIVE, width=27, height=1)
# display_label.place(x=10, y=10)
display_label = Label(root, font=("Arial", 20), fg=FG_COLOR, bg=BG_COLOR_ACTIVE)
display_label.place(x=B_X+(B_PADDING*0), y=5, width=410, height=60)

one_button = Button(root, text='1', font=("Arial", 20), fg=FG_COLOR, bg=BG_COLOR,
                    activeforeground=FG_COLOR_ACTIVE, activebackground=BG_COLOR_ACTIVE, highlightthickness=0,
                    command=lambda: entry_text(1))
one_button.place(x=B_X+(B_PADDING*0), y=B_Y+(B_PADDING*3), width=B_WIDTH, height=B_HEIGHT)
two_button = Button(root, text='2', font=("Arial", 20), fg=FG_COLOR, bg=BG_COLOR,
                    activeforeground=FG_COLOR_ACTIVE, activebackground=BG_COLOR_ACTIVE, highlightthickness=0,
                    command=lambda: entry_text(2))
two_button.place(x=B_X+(B_PADDING*1), y=B_Y+(B_PADDING*3), width=B_WIDTH, height=B_HEIGHT)
three_button = Button(root, text='3', font=("Arial", 20), fg=FG_COLOR, bg=BG_COLOR,
                      activeforeground=FG_COLOR_ACTIVE, activebackground=BG_COLOR_ACTIVE, highlightthickness=0,
                      command=lambda: entry_text(3))
three_button.place(x=B_X+(B_PADDING*2), y=B_Y+(B_PADDING*3), width=B_WIDTH, height=B_HEIGHT)
four_button = Button(root, text='4', font=("Arial", 20), fg=FG_COLOR, bg=BG_COLOR,
                     activeforeground=FG_COLOR_ACTIVE, activebackground=BG_COLOR_ACTIVE, highlightthickness=0,
                     command=lambda: entry_text(4))
four_button.place(x=B_X+(B_PADDING*0), y=B_Y+(B_PADDING*2), width=B_WIDTH, height=B_HEIGHT)
five_button = Button(root, text='5', font=("Arial", 20), fg=FG_COLOR, bg=BG_COLOR,
                     activeforeground=FG_COLOR_ACTIVE, activebackground=BG_COLOR_ACTIVE, highlightthickness=0,
                     command=lambda: entry_text(5))
five_button.place(x=B_X+(B_PADDING*1), y=B_Y+(B_PADDING*2), width=B_WIDTH, height=B_HEIGHT)
six_button = Button(root, text='6', font=("Arial", 20), fg=FG_COLOR, bg=BG_COLOR,
                    activeforeground=FG_COLOR_ACTIVE, activebackground=BG_COLOR_ACTIVE, highlightthickness=0,
                    command=lambda: entry_text(6))
six_button.place(x=B_X+(B_PADDING*2), y=B_Y+(B_PADDING*2), width=B_WIDTH, height=B_HEIGHT)
seven_button = Button(root, text='7', font=("Arial", 20), fg=FG_COLOR, bg=BG_COLOR,
                      activeforeground=FG_COLOR_ACTIVE, activebackground=BG_COLOR_ACTIVE, highlightthickness=0,
                      command=lambda: entry_text(7))
seven_button.place(x=B_X+(B_PADDING*0), y=B_Y+(B_PADDING*1), width=B_WIDTH, height=B_HEIGHT)
eight_button = Button(root, text='8', font=("Arial", 20), fg=FG_COLOR, bg=BG_COLOR,
                      activeforeground=FG_COLOR_ACTIVE, activebackground=BG_COLOR_ACTIVE, highlightthickness=0,
                      command=lambda: entry_text(8))
eight_button.place(x=B_X+(B_PADDING*1), y=B_Y+(B_PADDING*1), width=B_WIDTH, height=B_HEIGHT)
nine_button = Button(root, text='9', font=("Arial", 20), fg=FG_COLOR, bg=BG_COLOR,
                     activeforeground=FG_COLOR_ACTIVE, activebackground=BG_COLOR_ACTIVE, highlightthickness=0,
                     command=lambda: entry_text(9))
nine_button.place(x=B_X+(B_PADDING*2), y=B_Y+(B_PADDING*1), width=B_WIDTH, height=B_HEIGHT)
zero_button = Button(root, text='0', font=("Arial", 20), fg=FG_COLOR, bg=BG_COLOR,
                     activeforeground=FG_COLOR_ACTIVE, activebackground=BG_COLOR_ACTIVE, highlightthickness=0,
                     command=lambda: entry_text(0))
zero_button.place(x=B_X+(B_PADDING*0), y=B_Y+(B_PADDING*4), width=(B_WIDTH*2)+10, height=B_HEIGHT)
dot_button = Button(root, text='.', font=("Arial", 20), fg=FG_COLOR, bg=BG_COLOR,
                    activeforeground=FG_COLOR_ACTIVE, activebackground=BG_COLOR_ACTIVE, highlightthickness=0,
                    command=lambda: entry_text('.'))
dot_button.place(x=B_X+(B_PADDING*2), y=B_Y+(B_PADDING*4), width=B_WIDTH, height=B_HEIGHT)
percent_button = Button(root, text='%', state=DISABLED, font=("Arial", 20), fg=FG_COLOR, bg=BG_COLOR,
                        activeforeground=FG_COLOR_ACTIVE, activebackground=BG_COLOR_ACTIVE, highlightthickness=0,
                        command=lambda: entry_text('%'))
percent_button.place(x=B_X+(B_PADDING*0), y=B_Y+(B_PADDING*0), width=B_WIDTH, height=B_HEIGHT)
divide_button = Button(root, text='/', font=("Arial", 20), fg=FG_COLOR, bg=BG_COLOR,
                       activeforeground=FG_COLOR_ACTIVE, activebackground=BG_COLOR_ACTIVE, highlightthickness=0,
                       command=lambda: entry_text('/'))
divide_button.place(x=B_X+(B_PADDING*1), y=B_Y+(B_PADDING*0), width=B_WIDTH, height=B_HEIGHT)
times_button = Button(root, text='*', font=("Arial", 20), fg=FG_COLOR, bg=BG_COLOR,
                      activeforeground=FG_COLOR_ACTIVE, activebackground=BG_COLOR_ACTIVE, highlightthickness=0,
                      command=lambda: entry_text('*'))
times_button.place(x=B_X+(B_PADDING*2), y=B_Y+(B_PADDING*0), width=B_WIDTH, height=B_HEIGHT)
minus_button = Button(root, text='-', font=("Arial", 20), fg=FG_COLOR, bg=BG_COLOR,
                      activeforeground=FG_COLOR_ACTIVE, activebackground=BG_COLOR_ACTIVE, highlightthickness=0,
                      command=lambda: entry_text('-'))
minus_button.place(x=B_X+(B_PADDING*3), y=B_Y+(B_PADDING*0), width=B_WIDTH, height=B_HEIGHT)
plus_button = Button(root, text='+', font=("Arial", 20), fg=FG_COLOR, bg=BG_COLOR,
                     activeforeground=FG_COLOR_ACTIVE, activebackground=BG_COLOR_ACTIVE, highlightthickness=0,
                     command=lambda: entry_text('+'))
plus_button.place(x=B_X+(B_PADDING*3), y=B_Y+(B_PADDING*1), width=B_WIDTH, height=(B_HEIGHT*2)+10)
equal_button = Button(root, text='=', font=("Arial", 20), fg=FG_COLOR, bg=BG_COLOR,
                      activeforeground=FG_COLOR_ACTIVE, activebackground=BG_COLOR_ACTIVE, highlightthickness=0,
                      command=equal_press)
equal_button.place(x=B_X+(B_PADDING*3), y=B_Y+(B_PADDING*3), width=B_WIDTH, height=(B_HEIGHT*2)+10)
c_button = Button(root, text='C', font=("Arial", 20), fg=FG_COLOR, bg=BG_COLOR,
                  activeforeground=FG_COLOR_ACTIVE, activebackground=BG_COLOR_ACTIVE, highlightthickness=0,
                  command=back_enter)
c_button.place(x=B_X+(B_PADDING*4)+20, y=B_Y+(B_PADDING*0), width=B_WIDTH, height=B_HEIGHT)
ac_button = Button(root, text='AC', font=("Arial", 20), fg=FG_COLOR, bg=BG_COLOR,
                   activeforeground=FG_COLOR_ACTIVE, activebackground=BG_COLOR_ACTIVE, highlightthickness=0,
                   width=B_WIDTH, height=B_HEIGHT, command=clear_enter)
ac_button.place(x=B_X+(B_PADDING*4)+20, y=B_Y+(B_PADDING*1), width=B_WIDTH, height=B_HEIGHT)
bracket_open_button = Button(root, text='(', font=("Arial", 20), fg=FG_COLOR, bg=BG_COLOR,
                             activeforeground=FG_COLOR_ACTIVE, activebackground=BG_COLOR_ACTIVE, highlightthickness=0,
                             command=lambda: entry_text('('))
bracket_open_button.place(x=B_X+(B_PADDING*4)+20, y=B_Y+(B_PADDING*2), width=B_WIDTH, height=B_HEIGHT)
bracket_close_button = Button(root, text=')', font=("Arial", 20), fg=FG_COLOR, bg=BG_COLOR,
                              activeforeground=FG_COLOR_ACTIVE, activebackground=BG_COLOR_ACTIVE, highlightthickness=0,
                              command=lambda: entry_text(')'))
bracket_close_button.place(x=B_X+(B_PADDING*4)+20, y=B_Y+(B_PADDING*3), width=B_WIDTH, height=B_HEIGHT)
change_sign_button = Button(root, text='+/-', font=("Arial", 20), fg=FG_COLOR, bg=BG_COLOR,
                            activeforeground=FG_COLOR_ACTIVE, activebackground=BG_COLOR_ACTIVE, highlightthickness=0,
                            command=sign_enter)
change_sign_button.place(x=B_X+(B_PADDING*4)+20, y=B_Y+(B_PADDING*4), width=B_WIDTH, height=B_HEIGHT)

terminal2 = Text(root, bg=BG_COLOR_ACTIVE, fg=FG_COLOR_ACTIVE,
                 font=('DejaVu Sans', 15),
                 bd=0,
                 highlightthickness=0)
terminal2.place(x=B_X+(B_PADDING*0), y=B_Y+(B_PADDING*5), width=410, height=120)

root.mainloop()
