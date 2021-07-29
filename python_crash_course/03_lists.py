#!/usr/bin/env python3

# import this

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
languages = ['python', 'c++', 'java', 'c#', 'css', 'go', 'curl', 'pascal', 'fortran', 'perl', 'php']

# sort - permanently
languages.sort()
print(languages)
languages.sort(reverse=True)
print(languages)

# sort temporarily
languages = ['python', 'c++', 'java', 'c#', 'css', 'go', 'curl', 'pascal', 'fortran', 'perl', 'php']
print(f"Sorted list: {sorted(languages)}")
print(f"Original list: {languages}")

# reverse list
languages.reverse()
print(f"Reverse list: {languages}")

# Length list
print(f"{len(languages)} items are of the list")





