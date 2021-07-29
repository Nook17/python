#!/usr/bin/env python3

import os, subprocess

path_to_file = ''

def Read():
    global path_to_file
    if path_to_file:
        print('If path: \033[96m', path_to_file, '\033[0m is correct press ENTER')
    path_to_file = input('Enter the file path to read: ') or path_to_file
    try:
        file = open(path_to_file, 'r')
        print('\n==========================================\n')
        print(file.read())
        print('\n==========================================\n')
    except(FileNotFoundError):
        print("\033[91m\nFile or Directory doesn't exist!\033[0m\n")
    #file.close()

def Write():
    global path_to_file
    if path_to_file:
        print('If path: \033[96m', path_to_file, '\033[0m is correct press ENTER')
    path_to_file = input('Enter the file path to write: ') or path_to_file
    if os.path.isfile(path_to_file):
        print("\033[91m\nThis file aleady exist!\033[0m\n")
    else:
        print('\033[93m\nCreate the new file.\033[0m\n')
    file = open(path_to_file, 'w')
    content = input('Enter text to file: ')
    file.write(content)
    print('\033[92m\nDone.\033[0m\n')
    file.close()

def Append():
    global path_to_file
    if path_to_file:
        print('If path: \033[96m', path_to_file, '\033[0m is correct press ENTER')
    path_to_file = input('Enter the file path to append: ') or path_to_file
    if os.path.isfile(path_to_file):
        file = open(path_to_file, 'a')
        content = input('\nEnter text to file: ')
        file.write('\n' + content)
        print('\033[92m\nDone.\033[0m\n')
        file.close()
        choose = input("Do You want append more text to this file [ y / n ]: ")
        if choose == 'y':
            Append()
        else:
            Menu_start()
    else:
        print("\033[91m\nThis file doesn't exist.\033[0m\n")

def Delete():
    path_to_file = input('Enter the file path to delete: ')
    if os.path.isfile(path_to_file):
        os.remove(path_to_file)
        print('\033[92m\nDone.\033[0m\n')
    else:
        print("\033[91m\nThis file doesn't exist.\033[0m\n")

def Dirlist():
    path_to_file = input('Enter the directory path to display: ')
    if os.path.exists(path_to_file):
        print('\n')
        sortlist = os.listdir(path_to_file)
        i = 0
        while i < len(sortlist):
            print(sortlist[i])
            i += 1
        print('\033[92m\nDone.\033[0m\n')
    else:
        print("\033[91m\nThis folder doesn't exist.\033[0m\n")

def Check():
    path_to_file = input('Enter the file path to check: ')
    if os.path.isfile(path_to_file):
        print('\033[92m\nFile Exist.\033[0m\n')
    else:
        print("\033[91m\nThis file doesn't exist.\033[0m\n")

def Clear_desktop():
    try:
        os.system('clear')
    except OSError:
        os.system('cls')

# --- Menu ---
def Menu_start():
    run = 1
    while run == 1:
        Clear_desktop()
        decision = input('''
 ------- Nook File Manager v. 1.0 -------\n
        1.  Read a file
        2.  Write to file
        3.  Append Text to a file
        4.  Delete a file
        5.  List file in a directory
        6.  Check file existece
        7.  Move a file
        8.  Copy a file
        9.  Create in a directory
        10. Delete a directory
        11. Open a program
        q.  Exit
        Your decision: ''')
        if decision == '1':
            Clear_desktop()
            print('--- Read a file ---\n')
            Read()
        if decision == '2':
            Clear_desktop()
            print('--- Write to file ---\n')
            Write()
        if decision == '3':
            Clear_desktop()
            print('--- Append Text to a file ---\n')
            Append()
        if decision == '4':
            Clear_desktop()
            print('--- Delete a file ---\n')
            Delete()
        if decision == '5':
            Clear_desktop()
            print('--- List file in a directory ---\n')
            Dirlist()
        if decision == '6':
            Clear_desktop()
            print('--- Check file existece ---\n')
            Check()
        if decision == '7':
            Clear_desktop()
            print('Move a file')
        if decision == '8':
            Clear_desktop()
            print('Copy a file')
        if decision == '9':
            Clear_desktop()
            print('Create in a directory')
        if decision == '10':
            Clear_desktop()
            print('Delete a directory')
        if decision == '11':
            Clear_desktop()
            print('Open a program')
        if decision == 'q':
            Clear_desktop()
            exit()
        run = int(input('1. Return to menu\n2. Exit \n'))
        if run == 2:
            Clear_desktop()
            exit()
Menu_start()
