#!/usr/bin/env python3

import random


NUM_DIGITS = 3
MAX_GUESSES = 10


def main():
    print('*** Bajgle game ***')

    while True:
        print('Guess number. You have 10 tries')
        secretNum = getSecretNum()
        print(secretNum)
        i = 1
        while i <= MAX_GUESSES:
            guess = input('> ')
            clues = getClues(secretNum, guess)
            print(clues)
            i += 1
            if clues == 'victory':
                break
        print('Correct number is: {}'.format(secretNum))
        print('Do You have play again ? (y, n): ')
        if not input().lower().startswith('y'):
            break
    print('See You later')


def getSecretNum():
    num_ten = list('0123456789')
    random.shuffle(num_ten)
    num_game = ''
    for i in range(NUM_DIGITS):
        num_game += num_ten[i]
    return num_game


def getClues(secretNum, guess):
    if secretNum == guess:
        return 'victory'
    clues = []
    for i in range(len(guess)):
        if secretNum[i] == guess[i]:
            clues.append('Femi')
        elif guess[i] in secretNum:
            clues.append('Piko')

    if len(clues) == 0:
        return 'Bajgle'

    return ' '.join(clues)


if __name__ == '__main__':
    main()
