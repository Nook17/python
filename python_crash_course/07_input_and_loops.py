#!/usr/bin/env python3

def keep_going():
    print('\nKeep going !!!\n')

prompt = 'You can Stay or Exit the program [S/e]: '
choose = input(prompt) or 's'
if choose == 's':
    keep_going()
elif choose == 'e':
    exit()
else:
    print('fuck off')

# --- move list items ---
old_list = ['kojo', 'kama', 'nook', 'amon', 'nook', 'fiolka', 'dosia', 'nook']
new_list = []

while old_list:
    current_item = old_list.pop()
    new_list.append(current_item)
print(f"New list -> {new_list}")

# --- remove 'nook' item form new_list[] ---
while 'nook' in new_list:
    new_list.remove('nook')
print(f"List without 'nook' -> {new_list}")


