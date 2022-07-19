#!/usr/bin/env python3

import math
import getpass
import random
import pygame
import os
import subprocess
import bext

from function_mars import auto, more_arg_dictionaries, more_arg_mix, more_arg_tuple, suma
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

# --- Variables ---
#getpass.getpass(prompt='Enter password getpass: ', stream=None)

bext.fg('red')  # black, red, green, yellow, blue, purple, cyan, white

a = getpass.getpass('Enter Password: ')
b = input("Whatever: ")
num1 = int(input("Number 1: "))
num2 = input("Number 2: ")
num2 = int(num2)                    # change type variable
tajne_haslo = "password"
bext.fg('reset')
# --- Strings & Numbers ---
print('%s' % (b))
print("to jest zmienna b: {}". format(b))
print(f"to jest zmienna b: {b}")
print("change strings:", a.capitalize(), b.upper())
print("space:", a+" "+b)
print("divade no float:", num1 // num2)                 # return integer result
print("variable 'Whatever' type:", type(b))
print("lenght string 'Whatever':", len(b))
print("convert integer to binary:", bin(num1))          # converting intiger to binary
print("convert integer to binary:", format(num1, 'b'))  # converting intiger to binary
print("convert integer to hex:", format(num1, '#x'))    # converting intiger to hexadecimal

# --- Boolean expression ---
print(1, num1 == 6)
print(2, num1 < num2 and num1 == 5 or num2 == 17)

# --- function --- https://docs.python.org/3/library/functions.html

# --- math -> library ---
print("sqrt:", num1, "=", math.sqrt(num1))
print('pi =', math.pi)

# --- function user ---
def nook(name):
    print("\033[94mthis is function Mr\033[0m", name)

nook("Arek")
auto("Astra")
more_arg_tuple(1, 34, 'nook', 'and more arg')
more_arg_dictionaries(a=1, b=34, c='nook', d='and more arg')
more_arg_mix(2, 54, 44, 43, 'nook', x='kojo', y='kama')
print("Sum num1 and num2 is:", suma(num1, num2))

# --- Conditions -> if ---
if a == tajne_haslo:
    print(bcolors.OKGREEN + "You go on" + bcolors.ENDC)
elif a == b:
    print(bcolors.WARNING + "You won on lottery" + bcolors.ENDC)
else:
    print(f"{bcolors.FAIL}You go to jail{bcolors.ENDC}")

# --- loop -> for, while ---
for i in range(num1):
    print("loop no.: ", i)

list = [x * 5 for x in (1, 2, 3)]   # a list item is assigned to the variable "x" and multiplied by 5
print(list)

x = 1
while x < 5:
    print('random no. to 100:', random.randint(1, 100))
    x += 1

# --- run programs ---    
# os.system('pacman -Qii bat')
subprocess.run(['ls -la'], shell=True)
# subprocess.run(["qutebrowser https://www.teleman.pl"], shell=True)
#output = stream.readlines()


# ---- Justify / ALign (left, mid, right) ----
print("{:<10}".format("Guido"))  # 'Guido     '
print("{:>10}".format("Guido"))  # '     Guido'
print("{:^10}".format("Guido"))  # '  Guido   '

print=input("\n\033[41mPress Enter to Exit\033[0m")
