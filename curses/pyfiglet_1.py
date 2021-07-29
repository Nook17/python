#!/usr/bin/env python3

import curses, time, pyfiglet
# from pyfiglet import Figlet

stdscr = curses.initscr()

curses.start_color()
curses.use_default_colors()

# banner = Figlet(font="slant").renderText("Nook17")
now = pyfiglet.figlet_format(time.strftime("%H : %M : %S"), font = "starwars" )

while True:
    # Iterate through the lines of the Figlet
    y = 0
    for line in now.split("\n"):
        stdscr.addstr(y, 10, line)
        y += 1

    stdscr.refresh()
