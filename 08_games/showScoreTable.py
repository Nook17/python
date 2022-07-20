#!/usr/bin/env python3
import bext


def main():
    setScore()


def showScoreTable(score):
    print("=" * 31, end='')
    i = 1
    for key, value in score.items():
        print(f"\n|{key:>15} |", end='')
        if value[0] == 0 and value[1] == 0:
            bext.fg('red')
        if value[0] > 0  and value[1] == 1:
            bext.fg('yellow')
        if value[0] > 0 and value[1] == 0:
            bext.fg('green')
        print(f"{value[0]:^7}", end='')
        bext.fg('reset')
        print("|", end='')
        if key != 'Upper Section 1' and key != 'Upper Bonus' and key != 'Upper Section 2' and key != 'GRAND TOTAL':
            print(f"{i:^4}", end='')
        else:
            i = 6
            print(f"{'':^4}", end='')
        print("|", end='')
        i += 1
    print('\n', end='')
    print("=" * 31)


def showDictionaries(score):
    for key, value in score.items():
        print('{} - {}'.format(key, value))


def countPoints(score):
    score['Ones'][0] += 1

def setScore():
    score = {'Ones': [2, 0], 'Twos': [0, 0], 'Threes': [6, 0], 'Fours': [0, 0], 'Fives': [5, 0], 'Sixes': [0, 0],
             'Upper Section 1': [13, 0], 'Upper Bonus': [0, 0], '3 of a kind': [0, 0], '4 of a kind': [0, 0],
             'Full House': [0, 0], 'Low Straight': [30, 1], 'High Straight': [0, 0], 'AllFive!': [0, 0],
             'Chance': [0, 0], 'Upper Section 2': [30, 0], 'GRAND TOTAL': [43, 0]}
    countPoints(score)
    showScoreTable(score)

    score2 = {'Ones': [2, 0],
              'Twos': [1, 0],
              'Threes': [0, 0]
              }
    # showDictionaries(score)

if __name__ == '__main__':
    main()
