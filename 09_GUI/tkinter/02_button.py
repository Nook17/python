#!/usr/bin/python3
from tkinter import *

window = Tk()

topFrame = Frame(window)
topFrame.pack()
bottomFrame = Frame(window)
bottomFrame.pack(side=BOTTOM)

button1 = Button(topFrame, text='Button_1', fg='red')
button2 = Button(topFrame, text='Button_2', fg='yellow')
button3 = Button(bottomFrame, text='Button_3', fg='purple')
button4 = Button(bottomFrame, text='Button_4', fg='blue')

button1.pack(side=LEFT)
button2.pack(side=RIGHT)
button3.pack(side=BOTTOM)
button4.pack(side=TOP)

window.mainloop()