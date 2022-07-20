#!/usr/bin/env python3
import random, bext

def main():
    print('Start')
    dices = lottery([], 5)
    countPoints(dices)
    keepDices = keep()
    for i in range(1):
        dices = lottery(keepDices, 5 - len(keepDices))
        countPoints(dices)
        keepDices = keep()
    dices = lottery(keepDices, 5 - len(keepDices))
    countPoints(dices)
    # choose(dices)
    # countPoints(dices)


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


def countPoints(dice):
    score = setScore(False)
    dice.sort()
    diceNoDuplicate = list(dict.fromkeys(dice))
    flag = 0
    for i in range(5):
        if dice[i] == 1 and score['Ones'][1] == 0:
            score['Ones'][0] += 1
        if dice[i] == 2 and score['Twos'][1] == 0:
            score['Twos'][0] += 2
        if dice[i] == 3 and score['Threes'][1] == 0:
            score['Threes'][0] += 3
        if dice[i] == 4 and score['Fours'][1] == 0:
            score['Fours'][0] += 4
        if dice[i] == 5 and score['Fives'][1] == 0:
            score['Fives'][0] += 5
        if dice[i] == 6 and score['Sixes'][1] == 0:
            score['Sixes'][0] += 6
    if score['Ones'][0] >= 3 or score['Twos'][0] >= 6 or score['Threes'][0] >= 9 or score['Fours'][0] >= 12 \
            or score['Fives'][0] >= 15 or score['Sixes'][0] >= 18 and score['3 of a kind'][1] == 0:
        score['3 of a kind'][0] = sum(dice)
    if score['Ones'][0] >= 4 or score['Twos'][0] >= 8 or score['Threes'][0] >= 12 or score['Fours'][0] >= 16 \
            or score['Fives'][0] >= 20 or score['Sixes'][0] >= 24 and score['4 of a kind'][1] == 0:
        score['4 of a kind'][0] = sum(dice)

    for i in range(1, 7):
        if dice.count(i) == 3:
            for j in range(1, 7):
                if j != i:
                    if dice.count(j) == 2 and score['Full House'][1] == 0:
                        score['Full House'][0] = 25
        if dice.count(i) == 5 and score['AllFive!'][1] == 0:
            score['AllFive!'][0] = 50

    for i in range(len(diceNoDuplicate)-1):
        if diceNoDuplicate[i] + 1 == diceNoDuplicate[i+1]:
            flag += 1
    if flag >= 3 and score['Low Straight'][1] == 0:
        score['Low Straight'][0] = 30
    if flag == 4 and score['High Straight'][1] == 0:
        score['High Straight'][0] = 40

    if score['Chance'][1] == 0:
        score['Chance'][0] = sum(dice)

    score['Upper Section 1'][0] = score['Ones'][0] + score['Twos'][0] + score['Threes'][0] + score['Fours'][0] \
                               + score['Fives'][0] + score['Sixes'][0]
    score['Upper Section 2'][0] = score['Upper Bonus'][0] + score['3 of a kind'][0] + score['4 of a kind'][0] \
                               + score['Full House'][0] + score['Low Straight'][0] + score['High Straight'][0] \
                               + score['AllFive!'][0] + score['Chance'][0]
    score['GRAND TOTAL'][0] = score['Upper Section 1'][0] + score['Upper Section 2'][0]

    showScoreTable(score)
    print('Choose the number')
    choose = input('> ')
    if choose.isdecimal() and 1 <= int(choose) <= 13:
        setScore(score)
        main()


def choose(dice):
    print('Choose the number')
    input('> ')
    score = setScore()
    dice.sort()
    diceNoDuplicate = list(dict.fromkeys(dice))
    flag = 0
    for i in range(5):
        if dice[i] == 1 and score['Ones'][1] == 0:
            score['Ones'][0] += 1
            score['Ones'][1] = 1
        if dice[i] == 2 and score['Twos'][1] == 0:
            score['Twos'][0] += 2
            score['Twos'][1] = 1
        if dice[i] == 3 and score['Threes'][1] == 0:
            score['Threes'][0] += 3
            score['Threes'][1] = 1
        if dice[i] == 4 and score['Fours'][1] == 0:
            score['Fours'][0] += 4
            score['Fours'][1] = 1
        if dice[i] == 5 and score['Fives'][1] == 0:
            score['Fives'][0] += 5
            score['Fives'][1] = 1
        if dice[i] == 6 and score['Sixes'][1] == 0:
            score['Sixes'][0] += 6
            score['Sixes'][1] = 1
    if score['Ones'][0] >= 3 or score['Twos'][0] >= 6 or score['Threes'][0] >= 9 or score['Fours'][0] >= 12 \
            or score['Fives'][0] >= 15 or score['Sixes'][0] >= 18 and score['3 of a kind'][1] == 0:
        score['3 of a kind'][0] = sum(dice)
        score['3 of a kind'][1] = 1
    if score['Ones'][0] >= 4 or score['Twos'][0] >= 8 or score['Threes'][0] >= 12 or score['Fours'][0] >= 16 \
            or score['Fives'][0] >= 20 or score['Sixes'][0] >= 24 and score['4 of a kind'][1] == 0:
        score['4 of a kind'][0] = sum(dice)
        score['4 of a kind'][1] = 1

    for i in range(1, 7):
        if dice.count(i) == 3:
            for j in range(1, 7):
                if j != i:
                    if dice.count(j) == 2 and score['Full House'][1] == 0:
                        score['Full House'][0] = 25
                        score['Full House'][1] = 1
        if dice.count(i) == 5 and score['AllFive!'][1] == 0:
            score['AllFive!'][0] = 50
            score['AllFive!'][1] = 1

    for i in range(len(diceNoDuplicate)-1):
        if diceNoDuplicate[i] + 1 == diceNoDuplicate[i+1]:
            flag += 1
    if flag >= 3 and score['Low Straight'][1] == 0:
        score['Low Straight'][0] = 30
        score['Low Straight'][1] = 1
    if flag == 4 and score['High Straight'][1] == 0:
        score['High Straight'][0] = 40
        score['High Straight'][1] = 1

    if score['Chance'][1] == 0:
        score['Chance'][0] = sum(dice)
        score['Chance'][1] = 1

    score['Upper Section 1'][0] = score['Ones'][0] + score['Twos'][0] + score['Threes'][0] + score['Fours'][0] \
                               + score['Fives'][0] + score['Sixes'][0]
    score['Upper Section 2'][0] = score['Upper Bonus'][0] + score['3 of a kind'][0] + score['4 of a kind'][0] \
                               + score['Full House'][0] + score['Low Straight'][0] + score['High Straight'][0] \
                               + score['AllFive!'][0] + score['Chance'][0]
    score['GRAND TOTAL'][0] = score['Upper Section 1'][0] + score['Upper Section 2'][0]


def setScore(score):
    if score:
        score = {'Ones': [2, 1], 'Twos': [0, 0], 'Threes': [0, 0], 'Fours': [0, 0], 'Fives': [0, 0], 'Sixes': [0, 0],
                 'Upper Section 1': [0, 0], 'Upper Bonus': [0, 0], '3 of a kind': [0, 0], '4 of a kind': [0, 0],
                 'Full House': [0, 0], 'Low Straight': [30, 1], 'High Straight': [0, 0], 'AllFive!': [0, 0],
                 'Chance': [0, 0], 'Upper Section 2': [0, 0], 'GRAND TOTAL': [0, 0]}
        print('-- choose ---')

    score = {'Ones': [0, 0], 'Twos': [0, 0], 'Threes': [0, 0], 'Fours': [0, 0], 'Fives': [0, 0], 'Sixes': [0, 0],
             'Upper Section 1': [0, 0], 'Upper Bonus': [0, 0], '3 of a kind': [0, 0], '4 of a kind': [0, 0],
             'Full House': [0, 0], 'Low Straight': [0, 0], 'High Straight': [0, 0], 'AllFive!': [0, 0],
             'Chance': [0, 0], 'Upper Section 2': [0, 0], 'GRAND TOTAL': [0, 0]}
    return score


if __name__ == '__main__':
    main()
