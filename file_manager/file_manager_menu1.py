#!/usr/bin/env python3

import os, subprocess, curses, time, shutil

menu = ['r.  Read a file',
        'w.  Write to file',
        'a.  Append Text to a file',
        'd.  Delete a file',
        'l.  List file in a directory',
        'k.  Check file existece',
        'm.  Move a file',
        'c.  Copy a file',
        '1.  Create in a directory',
        '2.  Delete a directory',
        'o.  Open a program']

path_to_file = ''


def Read(stdscr):
    pad = curses.newpad(50, 140)
    stdscr.clear()
    stdscr.box()
    global path_to_file
    if path_to_file:
        stdscr.addstr(1, 1, 'If path: ') 
        stdscr.addstr(path_to_file, curses.color_pair(2))
        stdscr.addstr(' is correct press ENTER')
    stdscr.addstr(2, 1, 'Enter the file path to read: ')
    path_to_file = stdscr.getstr() or path_to_file
    if os.path.isfile(path_to_file):
        try:
            file = open(path_to_file, 'r')
            stdscr.hline(4, 1, '-', 152)
            try:
                pad.addstr(file.read())
            except curses.error: pass
            pad.refresh( 0,0, 5,5, 40,140)
            stdscr.hline(curses.LINES - 3, 1, '-', 152)
        except(FileNotFoundError):
            stdscr.addstr(curses.LINES - 2, 1, "File or Directory doesn't exist!", curses.color_pair(3))
    else:
        stdscr.addstr(curses.LINES - 2, 1, "File doesn't exist!", curses.color_pair(3))



def Write(stdscr):
    stdscr.clear()
    stdscr.box()
    global path_to_file
    if path_to_file:
        stdscr.addstr(1, 1, 'If path: ') 
        stdscr.addstr(path_to_file, curses.color_pair(2))
        stdscr.addstr(' is correct press ENTER')
    stdscr.addstr(2, 1, 'Enter the file path to write: ')
    path_to_file = stdscr.getstr() or path_to_file
    if os.path.isfile(path_to_file):
        stdscr.addstr(curses.LINES - 2, 1, "This file aleady exist!", curses.color_pair(3))
    else:
        stdscr.addstr(curses.LINES - 2, 1, "Create the new file.", curses.color_pair(2))
    file = open(path_to_file, 'w')
    stdscr.addstr(4, 1, 'Enter text to file: ')
    content = stdscr.getstr()
    file.write(str(content, encoding='utf-8'))
    stdscr.hline(curses.LINES - 2, 1, ' ', 23)
    stdscr.addstr(curses.LINES - 2, 1, 'Done.', curses.color_pair(4))
    file.close()


def Append(stdscr):
    stdscr.clear()
    stdscr.box()
    global path_to_file
    if path_to_file:
        stdscr.addstr(1, 1, 'If path: ') 
        stdscr.addstr(path_to_file, curses.color_pair(2))
        stdscr.addstr(' is correct press ENTER')
    stdscr.addstr(2, 1, 'Enter the file path to append: ')
    path_to_file = stdscr.getstr() or path_to_file
    if os.path.isfile(path_to_file):
        file = open(path_to_file, 'a')
        stdscr.addstr(4, 1, 'Enter text to file: ')
        content = stdscr.getstr()
        file.write('\n' + str(content, encoding='utf-8'))
        stdscr.hline(curses.LINES - 2, 1, ' ', 23)
        stdscr.addstr(curses.LINES - 2, 1, 'Done.', curses.color_pair(4))
        file.close()

        stdscr.addstr(curses.LINES - 2, 7, " --- Do You want append more text to this file [ y / n ]: ---", curses.A_BLINK)
        choose = stdscr.getch()
        if choose in [89, 121]:             # Y - y
            Append(stdscr)
        else:
            main(stdscr)
    else:
        stdscr.addstr(curses.LINES - 2, 1, "This file aleady exist!", curses.color_pair(3))


def Delete(stdscr):
    stdscr.addstr(2, 1, 'Enter the file path to delete: ')
    path_to_file = stdscr.getstr()
    if os.path.isfile(path_to_file):
        os.remove(path_to_file)
        stdscr.addstr(curses.LINES - 2, 1, 'Done.', curses.color_pair(4))
    else:
        stdscr.addstr(curses.LINES - 2, 1, "This file doesn't exist!", curses.color_pair(3))


def Dirlist(stdscr):
    global path_to_file
    if not path_to_file:
        path_to_file = os.path.abspath(os.getcwd())
    stdscr.addstr(1, 1, 'If path: ') 
    stdscr.addstr(path_to_file, curses.color_pair(2))
    stdscr.addstr(' is correct press ENTER')
    stdscr.addstr(2, 1, 'Enter the file path to check: ')
    path_to_file = stdscr.getstr() or path_to_file
    if os.path.exists(path_to_file) and not os.path.isfile(path_to_file):
        sortlist = os.listdir(path_to_file)
        i = 0
        try:
            while i < len(sortlist):
                stdscr.addstr(i + 4, 2, sortlist[i])
                i += 1
        except curses.error:
            pass
        stdscr.addstr(curses.LINES - 2, 1, 'Done.', curses.color_pair(4))
    else:
        stdscr.addstr(curses.LINES - 2, 1, "This folder doesn't exist!", curses.color_pair(3))


def Check(stdscr):
    stdscr.addstr(2, 1, 'Enter the file path to check: ')
    path_to_file = stdscr.getstr()
    if os.path.isfile(path_to_file):
        stdscr.addstr(curses.LINES - 2, 1, 'File Exist.', curses.color_pair(4))
    else:
        stdscr.addstr(curses.LINES - 2, 1, "This file doesn't exist!", curses.color_pair(3))


def Move(stdscr):
    stdscr.addstr(2, 1, 'Enter source path: ')
    path_source = stdscr.getstr()
    stdscr.addstr(4, 1, 'Enter destination path: ')
    path_destination = stdscr.getstr()
    shutil.move(path_source, path_destination)
    if os.path.dirname(path_source) == os.path.dirname(path_destination):
        stdscr.addstr(curses.LINES - 2, 1, 'File renamed.', curses.color_pair(4))
    else:
        stdscr.addstr(curses.LINES - 2, 1, 'File moved.', curses.color_pair(4))

def Copy(stdscr):
    stdscr.addstr(2, 1, 'Enter source path: ')
    path_source = stdscr.getstr()
    stdscr.addstr(4, 1, 'Enter destination path: ')
    path_destination = stdscr.getstr()
    shutil.copy(path_source, path_destination)
    if os.path.dirname(path_source) == os.path.dirname(path_destination):
        stdscr.addstr(curses.LINES - 2, 1, 'File duplicated.', curses.color_pair(4))
    else:
        stdscr.addstr(curses.LINES - 2, 1, 'File copied.', curses.color_pair(4))


def Create_dir(stdscr):
    stdscr.addstr(2, 1, 'Enter the path or name new directory: ')
    path_to_file = stdscr.getstr()
    if not os.path.exists(path_to_file):
        os.mkdir(path_to_file)
        stdscr.addstr(curses.LINES - 2, 1, 'Directory has been created.', curses.color_pair(4))
    else:
        stdscr.addstr(curses.LINES - 2, 1, "Oops something went wrong!", curses.color_pair(3))


def Delete_dir(stdscr):
    stdscr.addstr(2, 1, 'Enter the path of directory: ')
    path_to_file = stdscr.getstr()
    if os.path.exists(path_to_file) and len(os.listdir(path_to_file)) == 0:
        os.rmdir(path_to_file)
        stdscr.addstr(curses.LINES - 2, 1, 'Directory has been deleted.', curses.color_pair(4))
    elif os.path.exists(path_to_file) and len(os.listdir(path_to_file)) != 0:
        stdscr.addstr(curses.LINES - 2, 1, "This folder isn't empty. Do you want to delete it [ y / n ]", curses.color_pair(2))
        choose = stdscr.getch()
        if choose in [89, 121]:             # Y - y
            shutil.rmtree(path_to_file)
            stdscr.hline(curses.LINES - 2, 1, ' ', 60)
            stdscr.addstr(curses.LINES - 2, 1, 'Directory has been deleted.', curses.color_pair(4))
        else:
            main(stdscr)
    else:
        stdscr.addstr(curses.LINES - 2, 1, "This folder doesn't exist!", curses.color_pair(3))


def Open(stdscr):
    stdscr.addstr(2, 1, 'Enter the name of program: ')
    name_program = stdscr.getstr()
    try:
        # os.startfile(path_to_file)
        # os.open(str(path_to_file, encoding='utf-8'))
        # subprocess.call(str(name_program, encoding='utf-8'))
        subprocess.call(name_program)
    except:
        stdscr.addstr(curses.LINES - 2, 1, "File not found!", curses.color_pair(3))

# --- Menu ---
def Print_menu(stdscr, selected_row_idx):
    stdscr.clear()
    header = 'File Manager - ver. 1.1'
    footer_l = 'Key Command : q - to quit'
    footer_r = 'arek@nook17.pl'

    for idx, row in enumerate(menu):
        h, w = stdscr.getmaxyx()    # h - num_rows     w - num_cols
        x = w//2 - len(menu)//2
        y = h//2 - len(menu)//2 + idx
        x_h = w//2 - len(header)//2
        x_fr = w - len(footer_r) - 2
        if idx == selected_row_idx:
            stdscr.addstr(1, 1, ' ' * (w-1), curses.color_pair(1))
            stdscr.addstr(h-2, 0, ' ' * (w-1), curses.color_pair(1))
            stdscr.addstr(1, x_h, header, curses.color_pair(1))
            stdscr.addstr(h-2, 2, footer_l, curses.color_pair(1))
            stdscr.addstr(h-2, x_fr, footer_r, curses.color_pair(1))
            stdscr.attron(curses.color_pair(1))
            stdscr.addstr(y, x, row)
            stdscr.attroff(curses.color_pair(1))
            stdscr.box()
        else:
            stdscr.addstr(y, x, row)

    stdscr.refresh()


def main(stdscr):
    curses.curs_set(0)
    curses.echo()
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)
    curses.init_pair(2, curses.COLOR_YELLOW, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(4, curses.COLOR_GREEN, curses.COLOR_BLACK)

    current_row_idx = 0

    Print_menu(stdscr, current_row_idx)

    while 1:
        key = stdscr.getch()
        stdscr.clear()

        if key == curses.KEY_UP and current_row_idx > 0:
            current_row_idx -= 1
        elif key == curses.KEY_DOWN and current_row_idx < len(menu)-1:
            current_row_idx += 1
        elif key in [82, 114]:                                  # R - r
            Read(stdscr)
        elif key in [87, 119]:                                  # W - w
            Write(stdscr)
        elif key in [65, 97]:                                   # A - a
            Append(stdscr)
        elif key in [68, 100]:                                  # D - d
            Delete(stdscr)
        elif key in [76, 108]:                                  # L - l
            Dirlist(stdscr)
        elif key in [75, 107]:                                  # K - k
            Check(stdscr)
        elif key in [77, 109]:                                  # M - m
            Move(stdscr)
        elif key in [67, 99]:                                   # C - c
            Copy(stdscr)
        elif key in [49]:                                       # 1
            Create_dir(stdscr)
        elif key in [50]:                                       # 2
            Delete_dir(stdscr)
        elif key in [79, 111]:                                  # O - o
            Open(stdscr)
        elif key in [81, 113]:                                  # Q - q    
            exit()
        elif key == curses.KEY_ENTER or key in [10, 13]:        # LF - CR
            # if current_row_idx == len(menu) - 1:
                # exit()
            stdscr.box()
            if current_row_idx == 0:
                Read(stdscr)
            elif current_row_idx == 1:
                Write(stdscr)
            elif current_row_idx == 2:
                Append(stdscr)
            elif current_row_idx == 3:
                Delete(stdscr)
            elif current_row_idx == 4:
                Dirlist(stdscr)
            elif current_row_idx == 5:
                Check(stdscr)
            elif current_row_idx == 6:
                Move(stdscr)
            elif current_row_idx == 7:
                Copy(stdscr)
            elif current_row_idx == 8:
                Create_dir(stdscr)
            elif current_row_idx == 9:
                Delete_dir(stdscr)
            elif current_row_idx == 10:
                Open(stdscr)
            stdscr.refresh()
            key = stdscr.getch()

        Print_menu(stdscr, current_row_idx)
        stdscr.refresh()

curses.wrapper(main)
