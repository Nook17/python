#!/usr/bin/env python3
import json, bext


def main():
    # score = {"Nook": 17, "Kojo": 23, "Kama": 21, "Amon": 0}
    name = input('Type Your name: ')
    # checkNameScore(name)
    # printScoreTable(name)
    # saveScore(score)
    # openScore()
    endGame(117, name)


def saveScore(score):
    with open('score.txt', 'w') as file:
        file.write(json.dumps(score))     # use 'json.loads' to do the reverse


def openScore():
    f = open('score.txt')   # opening JSON file
    data = json.load(f)     # returns JSON object as a dictionary
    f.close()               # closing file
    return data


def printScoreTable(name):
    data = openScore()

    # for key, value in data.items():
    #     print('{} => {}'.format(key, value))

    # print('------------ S O R T E D ----------')
    sorted_data = {}
    sorted_keys = sorted(data, key=data.get)

    for w in sorted_keys:
        sorted_data[w] = data[w]

    for key, value in sorted_data.items():
        if key == name:
            bext.fg('yellow')
        else:
            bext.fg('reset')
        print('{} => {}'.format(key, value))
        bext.fg('reset')


def checkNameScore(name):
    score = openScore()
    if name in score:
        bext.fg('green')
        print('Hello {} Your maximum score is {}'.format(name, score[name]))
    else:
        bext.fg('cyan')
        print('Welcome first time {}'.format(name))
    bext.fg('reset')


def endGame(score, name):
    # global name
    if score == 117:
        data = openScore()

        if name in data:
            if data[name] < score:
                data[name] = score
                saveScore(data)
                print('Great. You beat your record !')
            else:
                print('Excellent {} Your score is {}'.format(name, score))
        else:
            data[name] = score
            saveScore(data)
            print('Congratulations on the first result of {} points'.format(score))
        printScoreTable(name)
        while True:
            print("'s' - start game again or 'q' - quit")
            choose = input('> ').upper()
            if choose == 'S':
                main()
            elif choose == 'Q':
                exit()
    else:
        return


if __name__ == '__main__':
    main()
