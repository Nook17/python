#!/usr/bin/env python3

import curses

bar = ' '   # with reverse video a space will show up
value1 = 10  # in real life this needs to be scaled

stdscr = curses.initscr()
curses.curs_set(0) # don't show the cursor

stdscr.addstr(1,3, "Python Curses Bar")
stdscr.refresh()
# Define windows 
win1 = curses.newwin(3, 32, 3, 2)
win1.border(0)  # add a border
# a horizontal bar 10 characters wide
win1.addstr(1, 1, bar * value1,curses.A_REVERSE )
win1.refresh()

# Wait for a key press then exit
stdscr.getch()
curses.endwin() # restore the terminal to original settings
