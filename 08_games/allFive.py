#!/usr/bin/env python3
import random, bext

def main():
    dices = lottery([], 5)
    countPoints(dices)
    keepDices = keep()
    for i in range(1):
        dices = lottery(keepDices, 5 - len(keepDices))
        countPoints(dices)
        keepDices = keep()
    dices = lottery(keepDices, 5 - len(keepDices))
    countPoints(dices)


def lottery(dices, length):
    for i in range(length):
        d = random.randint(1, 6)
        dices.append(d)
    print(dices)
    return dices


def keep():
    print('keep dice, e.g. > 566')
    keep = input('> ')
    keep = list(map(int, keep))

    return keep


def showScoreTable(score):
    print("=" * 29, end='')
    for key, value in score.items():
        print(f"\n|{key:>15} |", end='')
        if value == 0:
            bext.fg('red')
        else:
            bext.fg('green')
        print(f"{value:^10}", end='')
        bext.fg('reset')
        print(f" {'|':<2}", end='')
    print('\n', end='')
    print("=" * 29)


def countPoints(dice):
    score = setScore()
    dice.sort()
    diceNoDuplicate = list(dict.fromkeys(dice))
    flag = 0
    for i in range(5):
        if dice[i] == 1:
            score['Ones'] += 1
        if dice[i] == 2:
            score['Twos'] += 2
        if dice[i] == 3:
            score['Threes'] += 3
        if dice[i] == 4:
            score['Fours'] += 4
        if dice[i] == 5:
            score['Fives'] += 5
        if dice[i] == 6:
            score['Sixes'] += 6
    if score['Ones'] >= 3 or score['Twos'] >= 6 or score['Threes'] >= 9 or score['Fours'] >= 12 \
            or score['Fives'] >= 15 or score['Sixes'] >= 18:
        score['3 of a kind'] = sum(dice)
    if score['Ones'] >= 4 or score['Twos'] >= 8 or score['Threes'] >= 12 or score['Fours'] >= 16 \
            or score['Fives'] >= 20 or score['Sixes'] >= 24:
        score['4 of a kind'] = sum(dice)

    for i in range(1, 7):
        if dice.count(i) == 3:
            for j in range(1, 7):
                if j != i:
                    if dice.count(j) == 2:
                        score['Full House'] = 25
        if dice.count(i) == 5:
            score['AllFive!'] = 50

    for i in range(len(diceNoDuplicate)-1):
        if diceNoDuplicate[i] + 1 == diceNoDuplicate[i+1]:
            flag += 1
    if flag >= 3:
        score['Low Straight'] = 30
    if flag == 4:
        score['High Straight'] = 40

    score['Chance'] = sum(dice)

    score['Upper Section 1'] = score['Ones'] + score['Twos'] + score['Threes'] + score['Fours'] \
                               + score['Fives'] + score['Sixes']
    score['Upper Section 2'] = score['Upper Bonus'] + score['3 of a kind'] + score['4 of a kind'] \
                               + score['Full House'] + score['Low Straight'] + score['High Straight'] \
                               + score['AllFive!'] + score['Chance']
    score['GRAND TOTAL'] = score['Upper Section 1'] + score['Upper Section 2']

    showScoreTable(score)


def setScore():
    score = {'Ones': 0, 'Twos': 0, 'Threes': 0, 'Fours': 0, 'Fives': 0, 'Sixes': 0, 'Upper Section 1': 0,
             'Upper Bonus': 0, '3 of a kind': 0, '4 of a kind': 0, 'Full House': 0, 'Low Straight': 0,
             'High Straight': 0, 'AllFive!': 0, 'Chance': 0, 'Upper Section 2': 0, 'GRAND TOTAL': 0}
    return score


if __name__ == '__main__':
    main()
