#!/usr/bin/env python3

import curses, time

def main(stdscr):
    curses.curs_set(0)
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)

    h, w = stdscr.getmaxyx()
    text = "Nook17.pl"

    x = w//2 - len(text)//2
    y= h//2

    stdscr.attron(curses.color_pair(1))
    stdscr.addstr(y, x, text)
    stdscr.attroff(curses.color_pair(1))

    stdscr.refresh()
    time.sleep(3)

curses.wrapper(main)
