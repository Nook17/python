#!/usr/bin/env python3

import curses

def main(stdscr):
    stdscr = curses.initscr()
    curses.echo()
    row, col = stdscr.getmaxyx()
    x = col//2
    y = row//2

    stdscr.addstr(1, 1, 'Enter txt: ')
    txt = stdscr.getstr()

    stdscr.addstr(txt, curses.A_ITALIC)
    stdscr.refresh()

    stdscr.getch()

    curses.endwin()

curses.wrapper(main)
