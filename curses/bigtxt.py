#!/usr/bin/env python3

import curses, time
import pyfiglet, random

def get_io(): # Get a random value. Tweek later with real data
    global value1
    # testvalue = str(random.randint(100,1000)/10) + " C"
    testvalue = 'Nook17'
    value1 = pyfiglet.figlet_format(testvalue, font = "starwars" )

# Create a string of text based on the Figlet font object
title = pyfiglet.figlet_format("Menu Arka Demko", font = "small" )

stdscr = curses.initscr() # create a curses object
# Create a couple of color definitions
curses.start_color()
curses.init_pair(1, curses.COLOR_YELLOW, curses.COLOR_BLACK)
curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)

# Write the BIG TITLE text string
stdscr.addstr(1,0, title,curses.color_pair(1) )
stdscr.addstr(8,0, "Sensor 1: GPIO 7 Temperature Reading" ,curses.A_BOLD)

# Cycle getting new data, enter a 'q' to quit
stdscr.nodelay(1)
k = 0
while (k != ord('q')):
    get_io() # get the data values
    stdscr.addstr(10,0, value1,curses.color_pair(2) )
    stdscr.refresh()
    time.sleep(2)

    k = stdscr.getch()

curses.endwin()
