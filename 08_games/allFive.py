#!/usr/bin/env python3
import random


def main():
    print(lottery())
    # print(showScore())
    score = {'Ones': 0, 'Twos': 0, 'Threes': 0, 'Fours': 0, 'Fives': 0, 'Sixes': 0, 'Upper Section': 0, 'Upper Bonus': 0,
             '3 of a kind': 0, '4 of a kind': 0, 'Full House': 0, 'Low Straight': 0, 'High Straight': 0, 'AllFive!': 0,
             'Chance': 0, 'GRAND TOTAL': 0}
    print(make_table(score))


def lottery():
    dices = []
    for i in range(5):
        d = random.randint(1, 6)
        dices.append(d)
    return dices


def showScore():
    score = {'Ones': 0, 'Twos': 0, 'Threes': 0, 'Fours': 0, 'Fives': 0, 'Sixes': 0, 'Upper Section': 0, 'Upper Bonus': 0,
             '3 of a kind': 0, '4 of a kind': 0, 'Full House': 0, 'Low Straight': 0, 'High Straight': 0, 'AllFive!': 0,
             'Chance': 0, 'GRAND TOTAL': 0}
    for key, value in score.items():
        print('{} - {}'.format(key, value))


def make_table(score):
    s = "=" * 29
    for key, value in score.items():
        s += f"\n|{key:>15} |{value:^10}{'|':<2}"
    s += '\n'
    s += "=" * 29
    return s


if __name__ == '__main__':
    main()
'''
Throw dice, keep dice
Ones
Twos
Threes
Fours
Fives
Sixes
Upper Section
Upper Bonus
-------
3 of a kind
4 of a kind
Full House
Low Straight
High Straight
AllFive!
Chance
GRAND TOTAL
'''
