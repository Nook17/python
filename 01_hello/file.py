#!/usr/bin/env python3

import time

# --- Open file ---
bitcoin = open('/home/arek/magazyn/projects/python/01_hello/example.txt')
print(bitcoin.read(12))         # read 12 characters
print(bitcoin.readline())       # read 1'st paragtaph
line = bitcoin.readlines()
print(line[1])

# for line in line:
#     print(line)
#     time.sleep(.20)

# --- Write to file ---
data_file = open("/home/arek/magazyn/projects/python/01_hello/write_file.txt", "w")     # open file witch write flag
data_file.write('100, 20, 17')
print(data_file.writable())
data_file.close()
data_file = open("/home/arek/magazyn/projects/python/01_hello/write_file.txt", "a")     # open file witch access or append flag
data_file.write("\n23, 45, 255\n")
data_file.close()
data_file = open("/home/arek/magazyn/projects/python/01_hello/write_file.txt", "r+")     # open file witch read and write flag
data_file.write("0, 2, 15\n")
c = data_file.readlines()
data_file.close()
data_file = open("/home/arek/magazyn/projects/python/01_hello/write_file.txt", "r")     # open file witch read flag
# content = data_file.readlines()
# print(content)
#for i in content:
for i in data_file:
    print(i)
data_file.close()

# --- Exceptions ---
try:
    a = int(input('Input first No.: '))
    b = int(input('Input Second No.: '))
    print(a / b)
except ZeroDivisionError:
    print('\033[91mYou have tried to divide to by Zero!\033[0m')
else:
    print("\033[92mYou didn't divide by Zero. Well done!\033[0m")


try:
    data_file = open("/home/arek/magazyn/projects/python/01_hello/write_file.txt", "r")
    data_file.write("This is a test.")
except IOError:
    print("\033[91mError: unable to write the file. Check permissions\033[0m")
else:
    print("\033[92mContent written to file seccessfully. Have nice day.\033[0m")
    data_file.close()

"""
'r' open for reading (default)
'w' open for writing, truncating the file first
'x' open for exclusive creation, failing if the file already exists
'a' open for writing, appending to the end of the file if it exists
----
'b' binary mode
't' text mode (default)
'+' open a disk file for updating (reading and writing)
'U' universal newlines mode (for backwards compatibility; should not be used in new code)

Thus the modes for opening a file should be:
rt / wt / xt / at for reading / writing / creating / appending to a file in text mode and
rb / wb / xb / ab for reading / writing / creating / appending to a file in binary mode.
"""


