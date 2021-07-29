#!/usr/bin/env python3

import curses, pyfiglet, time

def main(stdscr):
    stdscr = curses.initscr()
    curses.noecho()         # hidden put text
    curses.curs_set(0)      # hidden cursor
    stdscr.nodelay(1)

    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_YELLOW, curses.COLOR_BLACK)

    while 1:
        row, col = stdscr.getmaxyx()
        now = pyfiglet.figlet_format(time.strftime("%H : %M : %S"), font = "starwars" )
        today = time.strftime("%d %B %Y - %A")
        x_scr_n = col//2 - (len(now)//8)//2
        x_scr_t = col//2 - len(today)//2 + 2
        y_scr_n = row//2 - 4
    
        stdscr.clear()
        # now = pyfiglet.figlet_format(time.strftime("%H : %M : %S"), font = "starwars")
        y = 0
        for line in now.split("\n"):
            stdscr.addstr(y_scr_n + y, x_scr_n, line, curses.color_pair(1))
            y += 1
        stdscr.addstr(y_scr_n + 7, x_scr_t, today, curses.color_pair(2))
        stdscr.refresh()
        time.sleep(0.1)
        if stdscr.getch() == ord('q'):
            break

    curses.endwin()

curses.wrapper(main)
