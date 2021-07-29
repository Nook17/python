#!/usr/bin/env python3

import random

lotto = 0

def Enter_number():
    number = int(input('Enter a number from 1 to 30: '))
    Check_enter_number(number)


def Check_enter_number(number):
    global lotto
    if 0 < number <= 30:
        if lotto:
            Are_you_win(number, lotto)
        else:
            lotto = Random_number()
            Are_you_win(number, lotto)
    else:    
        print('number out of range!. Enter again')
        Enter_number()


def Are_you_win(number, lotto):
    # print('you = ', number)
    # print('Lotto = ', lotto)
    if number > lotto:
        print('Your number is too big. Try again')
        Enter_number()
    elif number < lotto:
        print('Your number is too small. Try again')
        Enter_number()
    elif number == lotto:
        print('You are win !!!')


def Random_number():
    return random.randrange(1, 30)
    Enter_number()


def main():
    Enter_number()


main()

