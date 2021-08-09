#!/usr/bin/env python3

# --- Reading from a file ---
with open('txt_files/arek.txt', 'r') as file_object:  # 'with' doesn't required close()
    content = file_object.read()
print(content.rstrip()) # 'rstrip()' remove empty string from the end of the file

