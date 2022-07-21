#!/usr/bin/env python3
import random, bext
from collections import Counter

setFlag = 0
scoreChoose = {'Ones': [0, 0], 'Twos': [0, 0], 'Threes': [0, 0], 'Fours': [0, 0], 'Fives': [0, 0], 'Sixes': [0, 0],
         'Upper Section 1': [0, 0], 'Upper Bonus': [0, 0], '3 of a kind': [0, 0], '4 of a kind': [0, 0],
         'Full House': [0, 0], 'Low Straight': [0, 0], 'High Straight': [0, 0], 'AllFive!': [0, 0],
         'Chance': [0, 0], 'Upper Section 2': [0, 0], 'GRAND TOTAL': [0, 0]}


def main():
    game()


def game():
    print(' -------- Start Game --------')
    round = 1
    dices = lottery([], 5)
    countPoints(dices, round)
    keepDices = keep()
    for i in range(1):
        round += 1
        dices = lottery(keepDices, 5 - len(keepDices))
        countPoints(dices, round)
        keepDices = keep()
    dices = lottery(keepDices, 5 - len(keepDices))
    round = 3
    countPoints(dices, round)


def lottery(dices, length):
    for i in range(length):
        d = random.randint(1, 6)
        dices.append(d)
    print(dices, end='')
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
        if value[1] == 1:
            bext.fg('yellow')
        if value[0] > 0 and value[1] == 0:
            bext.fg('green')
        if key == 'Upper Section 1' or key == 'Upper Section 2' or key == 'GRAND TOTAL':
            bext.fg('purple')
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


def countPoints(dice, round):
    score = setScore()
    print('      Round: {}'.format(round))
    dice.sort()
    diceNoDuplicate = list(dict.fromkeys(dice))
    flag = 0
    score = zeroScore(score)
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

    sameElement = dict(Counter(dice))
    for value in sameElement.values():
        if value >= 3 and score['3 of a kind'][1] == 0:
            score['3 of a kind'][0] = sum(dice)
        if value >= 4 and score['4 of a kind'][1] == 0:
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

    # score['Upper Section 1'][0] = score['Ones'][0] + score['Twos'][0] + score['Threes'][0] + score['Fours'][0] \
    #                            + score['Fives'][0] + score['Sixes'][0]
    score['Upper Section 1'][0] = 0
    if score['Ones'][1] == 1:
        score['Upper Section 1'][0] += score['Ones'][0]
    if score['Twos'][1] == 1:
        score['Upper Section 1'][0] += score['Twos'][0]
    if score['Threes'][1] == 1:
        score['Upper Section 1'][0] += score['Threes'][0]
    if score['Fours'][1] == 1:
        score['Upper Section 1'][0] += score['Fours'][0]
    if score['Fives'][1] == 1:
        score['Upper Section 1'][0] += score['Fives'][0]
    if score['Sixes'][1] == 1:
        score['Upper Section 1'][0] += score['Sixes'][0]

    if score['Upper Section 1'][0] >= 63:
        score['Upper Bonus'] = [35, 1]

    # score['Upper Section 2'][0] = score['Upper Bonus'][0] + score['3 of a kind'][0] + score['4 of a kind'][0] \
    #                            + score['Full House'][0] + score['Low Straight'][0] + score['High Straight'][0] \
    #                            + score['AllFive!'][0] + score['Chance'][0]
    score['Upper Section 2'][0] = 0
    if score['Upper Bonus'][1] == 1:
        score['Upper Section 2'][0] += score['Upper Bonus'][0]
    if score['3 of a kind'][1] == 1:
        score['Upper Section 2'][0] += score['3 of a kind'][0]
    if score['4 of a kind'][1] == 1:
        score['Upper Section 2'][0] += score['4 of a kind'][0]
    if score['Full House'][1] == 1:
        score['Upper Section 2'][0] += score['Full House'][0]
    if score['Low Straight'][1] == 1:
        score['Upper Section 2'][0] += score['Low Straight'][0]
    if score['High Straight'][1] == 1:
        score['Upper Section 2'][0] += score['High Straight'][0]
    if score['AllFive!'][1] == 1:
        score['Upper Section 2'][0] += score['AllFive!'][0]
    if score['Chance'][1] == 1:
        score['Upper Section 2'][0] += score['Chance'][0]

    score['GRAND TOTAL'][0] = score['Upper Section 1'][0] + score['Upper Section 2'][0]

    showScoreTable(score)
    while True:
        print("Choose the number or 'q' - quit")
        choose = input('> ')
        if choose == 'q':
            exit()
        if int(round) < 3:
            break
        if choose.isdecimal() and 1 <= int(choose) <= 13 and int(round) == 3:
            break

    if choose.isdecimal() and 1 <= int(choose) <= 13:
        if int(choose) == 1:
            chooseKey(True, 'Ones', score['Ones'][0])
        if int(choose) == 2:
            chooseKey(True, 'Twos', score['Twos'][0])
        if int(choose) == 3:
            chooseKey(True, 'Threes', score['Threes'][0])
        if int(choose) == 4:
            chooseKey(True, 'Fours', score['Fours'][0])
        if int(choose) == 5:
            chooseKey(True, 'Fives', score['Fives'][0])
        if int(choose) == 6:
            chooseKey(True, 'Sixes', score['Sixes'][0])
        if int(choose) == 7:
            chooseKey(True, '3 of a kind', score['3 of a kind'][0])
        if int(choose) == 8:
            chooseKey(True, '4 of a kind', score['4 of a kind'][0])
        if int(choose) == 9:
            chooseKey(True, 'Full House', score['Full House'][0])
        if int(choose) == 10:
            chooseKey(True, 'Low Straight', score['Low Straight'][0])
        if int(choose) == 11:
            chooseKey(True, 'High Straight', score['High Straight'][0])
        if int(choose) == 12:
            chooseKey(True, 'AllFive!', score['AllFive!'][0])
        if int(choose) == 13:
            chooseKey(True, 'Chance', score['Chance'][0])
        game()


def chooseKey(set, key='', value=0):
    # print('--- Choose ---')
    global setFlag
    if set:
        setFlag = 1
        scoreChoose[key] = [value, 1]
    return scoreChoose, setFlag


def setScore():
    # print('---- Game ----')
    getFlagTuple = chooseKey(False)
    getFlag = getFlagTuple[1]
    # print('Flag = {}'.format(getFlag))
    if getFlag == 1:
        scoreTuple = chooseKey(False)
        score = scoreTuple[0]
    else:
        score = {'Ones': [0, 0], 'Twos': [0, 0], 'Threes': [0, 0], 'Fours': [0, 0], 'Fives': [0, 0], 'Sixes': [0, 0],
                 'Upper Section 1': [0, 0], 'Upper Bonus': [0, 0], '3 of a kind': [0, 0], '4 of a kind': [0, 0],
                 'Full House': [0, 0], 'Low Straight': [0, 0], 'High Straight': [0, 0], 'AllFive!': [0, 0],
                 'Chance': [0, 0], 'Upper Section 2': [0, 0], 'GRAND TOTAL': [0, 0]}

    return score


def zeroScore(score):
    if score['Ones'][1] == 0:
        score['Ones'][0] = 0
    if score['Twos'][1] == 0:
        score['Twos'][0] = 0
    if score['Threes'][1] == 0:
        score['Threes'][0] = 0
    if score['Fours'][1] == 0:
        score['Fours'][0] = 0
    if score['Fives'][1] == 0:
        score['Fives'][0] = 0
    if score['Sixes'][1] == 0:
        score['Sixes'][0] = 0
    if score['3 of a kind'][1] == 0:
        score['3 of a kind'][0] = 0
    if score['4 of a kind'][1] == 0:
        score['4 of a kind'][0] = 0
    if score['Full House'][1] == 0:
        score['Full House'][0] = 0
    if score['Low Straight'][1] == 0:
        score['Low Straight'][0] = 0
    if score['High Straight'][1] == 0:
        score['High Straight'][0] = 0
    if score['AllFive!'][1] == 0:
        score['AllFive!'][0] = 0
    if score['Chance'][1] == 0:
        score['Chance'][0] = 0

    return score


if __name__ == '__main__':
    main()
