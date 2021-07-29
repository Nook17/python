#!/usr/bin/env python3

from turtle import *

# --- Circle ---
#turtle.circle(50, 180)

# --- Square ---
# turtle.color("Red", "yellow")
# turtle.shape("turtle")
# for t in range(4):
#     turtle.forward(100)
#     turtle.left(90)

# --- Shapes ---
color('red', 'yellow')
begin_fill()
while True:
    forward(200)
    left(170)
    if abs(pos()) < 1:
        break
    end_fill()
    done()


#turtle.getscreen()._root.mainloop()

# print=input('Press Enter to Exit')

