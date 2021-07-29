#!/usr/bin/env python3

# import this
import random

languages = ['python', 'c++', 'java', 'c#', 'css']
print(languages)
print(languages[-1])    # access to last element of the list

# --- add to list ---
languages.append('go')
print(languages)

languages.insert(2, 'java script')
print(languages)

# --- remove position by No. item ---
del languages[2]
print(languages)

pop_element = languages.pop()
print(pop_element)

pop_element = languages.pop(3)
print(pop_element)
print(languages)

# --- remove position by value name ---
languages.remove('c++')
print(languages)

# --- Organizing the list ---
languages = ['python', 'c++', 'java', 'c#', 'css', 'go', 'curl', 'pascal', 
             'fortran', 'perl', 'php']

# sort - permanently
languages.sort()
print(languages)
languages.sort(reverse=True)
print(languages)

# sort temporarily
languages = ['python', 'c++', 'java', 'c#', 'css', 'go', 'curl', 'pascal', 
             'fortran', 'perl', 'php']
print(f"Sorted list: {sorted(languages)}")
print(f"Original list: {languages}")

# reverse list
languages.reverse()
print(f"Reverse list: {languages}")

# Length list
print(f"{len(languages)} items are of the list\n")

# --- loop for ---
i = 1
for language in languages:
    print(f"{i}. {language}")
    i += 1

print("\n")
for i in range(1, 3):
    print(i)

# --- create list by range ---
print("\n")
number = list(range(1, 11))
print(number)

rand_number = []
square = []
for i in range(1, 11):
    rand_number.append((random.randrange(1, 11)))
    square.append(i ** 2)
print(rand_number)
print(square)

# Statistics
print(f"Max: {max(rand_number)}")
print(f"Min: {min(rand_number)}")
print(f"Sum: {sum(rand_number)}")

# List Comprehensions
comp_rand_number = [random.randrange(1, 11) for i in range(10)]
comp_square = [i ** 2 for i in range(1, 11)]
print(comp_rand_number)
print(comp_square)

# --- Part of List ---

# slice
languages = ['python', 'c++', 'java', 'c#', 'css', 'go', 'curl', 'pascal',
             'fortran', 'perl', 'php']
print(languages[0:3])       # when you start from the beginning you can write 
                            # [:3], or end of list [5:]
print(languages[-3:])       # last three items

# coping list
languages_copy = languages[:]
print(languages_copy)

# --- Tuples ---
print("\n TUPLES")
nook = (20, 17, 256)
print(nook[1])

