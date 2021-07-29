#!/usr/bin/env python3

import getpass
import json
import ast

status = ""
USERS = {}

def main_menu():
    load_file()
    status = input("Do you have a login account? y/n/q: ")
    if status == 'y':
        old_user()
    elif status == 'n':
        new_user()
    elif status == 'q':
        quit()

def load_file():
    global USERS
    with open("/home/arek/magazyn/projects/python/01_hello/login.txt", "r") as fr:  # Wyjątek przekazujący obiekt do uchwytu fr. ( Na koniec nie ma potrzeby zamykania pliku )
        data = fr.read()
    USERS = json.loads(data)                                    # konwersja json -> Dictionaries
    print(USERS)

def old_user():
    global USERS
    login = input('Enter Login: ')
    password = getpass.getpass('Enter password: ')
    if login in USERS and USERS[login] == password:
        print('You are logged')
    else:
        print('Login or password is wrong!')

def new_user():
    global USERS
    print(USERS)
    login = input('Enter Login: ')
    if login in USERS:
        print('Login', login, 'already exists')
    else:
        password = getpass.getpass('Enter password: ')
        USERS[login] = password
        print('Users Type: ', type(USERS))
        with open("/home/arek/magazyn/projects/python/01_hello/login.txt", "w") as fw:
            json.dump(USERS, fw)
    

while status != 'q':
    main_menu()
