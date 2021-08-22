#!/usr/bin/env python3

import json

# --- Reading from a file ---
with open('txt_files/arek.txt', 'r') as file_object:  # 'with' doesn't required close()
    content = file_object.read()
print(content.rstrip()) # 'rstrip()' remove empty string from the end of the file

# read file with for loop
print('\n')
filename = 'txt_files/arek.txt'
with open(filename, 'r') as file_object:
    for content in file_object:
        print(content.rstrip())

# making a List of lines from a File
print('\n')
with open(filename, 'r') as file_object:
    list = file_object.readlines()
for line in list:
    print(line.rstrip())
print(list)

# are you birthday appears in the pi ?
print('\n')
filename = 'txt_files/pi_million_digits.txt'
with open(filename, 'r') as file_object:
    list = file_object.readlines()
pi = ''
for line in list:
    pi += line.strip()
# birthday = input('Enter your birthday, in the form ddmmyy: ')
birthday = '221080'
if birthday in pi:
    print('Your birthday appears in first milion digits of pi')
else:
    print('Your birthday does not appears in the first milion digits of pi')

# --- Writing to a file ---
filename = 'txt_files/arek.txt'
textToFile = 'Attention, this is a radioactive area!'
with open(filename, 'w') as file_object:
    file_object.write(textToFile)

# ---------------------------------------------------------------
# --- Exceptions ---
print("\n--- Exceptions ---")
# ZeroDivisionError
print("\n--- ZeroDivisionError ---\n")
try:
    print(5 / 0)
except ZeroDivisionError:
    print('\033[91mYou can not division by ZERO !!!\033[0m')
# FileNotFoundError
print("\n--- FileNotFoundError ---\n")
fileName = 'txt_files/alice.tx_'    # this file doesn't exist
content = 'empty file'
try:
    with open(fileName, 'r', encoding='utf-8') as f:
        content = f.read()
except FileNotFoundError:
    print(f"\033[91mThe file \033[93m{fileName}\033[0m \033[91m\
does not exist !\033[0m")
else:
    list = content.split()
    wordsInText = len(list)
    print(f"The file {fileName} has about {wordsInText} words.")

# ---------------------------------------------------------------
# --- JSON ---
print("\n--- JSON ---")
# dump() & load()
numbers = [2, 5, 34, 32, 62, 323, 1256]
filename = 'txt_files/numbers.json'
with open(filename, 'w') as f:
    json.dump(numbers, f)
with open(filename, 'r') as f:
    numb = json.loads(f)
print(numb)


