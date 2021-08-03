#!/usr/bin/env python3

"""
import module_name
from module_name import function_name
from module_name import function_name as f_n
import module_name as m_n
from module_name import *

"""


def show(argument):     # function definition and arguments
    print(f"argument: {argument}\n")

show('parameters')      # function call and parameters

# --- Positional Arguments ---
def pos_arg(name, title):
    print(f"Title: {title} by {name}\n")

pos_arg('Eric Matthes', 'Python Crash Course')

# --- Keyword Arguments ---
def key_arg(title, name = 'noname'):
    print(f"Title: {title} by {name}\n")

key_arg(title = 'Python by Example', name = 'Nicola Lacey')
key_arg('Linux Grate way to success')

# --- Return Values ---
def sum(a, b):
    return a + b
a, b = 5, 10
print(f"Sum {a} and {b} is {sum(a, b)}\n")

# -----------
# !!! send copy list NOT original !!!
# function_name(list_name[:])
# -----------

# --- Passing an arbitrary Number of Arguments ---
def many_arg(yr, *args):
    print(f"Its {yr} year. Names -> {args}")    # Function returned TUPLES
many_arg(2021, 'arek', 'darek', 'marek')

# --- Arbitrary Keyword Arguments
def arb_key(age, **kwargs):
    print(f"Age {age} old. actor -> {kwargs}")  # Function returned DICTIONARY
arb_key(45, 
        fname = 'john', 
        lname2 = 'wick', 
        gun = 'walter')
