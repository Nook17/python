#!/usr/bin/env python3

# --- if statements ---
nook = "Kojo"
if nook.lower() == 'kojo':
    print("kojo is git\n")
else:
    print("Where is Kojo\n")

# Checking whether a value is in a LIST
nook = ['kojo', 'kama', 'amon']
if 'kojo' in nook:
    print('Kojo is on the list')
if 'arek' not in nook:
    print("Arek doesn't exist on the list")
else:
    print('I go to sleep')

list_test = ['aa']
print(bool(list_test))

# --- add numbers to list ---
number = []
count = 10
for i in range(count):
    if i + 1 == 1:
        number.append(f"{i + 1}st")
    elif i + 1 == 2:
        number.append(f"{i + 1}nd")
    elif i + 1 == 3:
        number.append(f"{i + 1}rd")
    else:
        number.append(f"{i + 1}th")
print(number)


