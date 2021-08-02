#!/usr/bin/env python3

def keep_going():
    print('\nKeep going !!!')

prompt = 'You can Stay or Exit the program [S/e]: '
choose = input(prompt) or 's'
if choose == 's':
    keep_going()
elif choose == 'e':
    exit()
else:
    print('fuck off')

