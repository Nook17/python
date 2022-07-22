#!/usr/bin/env python3
import random
# from collections import OrderedDict

def main():
    dices = lottery([], 5)
    # print(type(dices))
    keepDices = keep(dices)
    # for i in range(1):
    dices = lottery(keepDices, 5 - len(keepDices))
    keepDices = keep(dices)
    dices = lottery(keepDices, 5 - len(keepDices))
    keepDices = keep(dices)
    lottery(keepDices, 5 - len(keepDices))
    # print(dices)

def lottery(dices, length):
    # dices = []
    for i in range(length):
        d = random.randint(1, 6)
        dices.append(d)
    # dices.sort()
    print(dices)
    return dices


def keep(dices):
    print('keep dice, e.g. > 566')
    while True:
        keep = input('> ')
        keep = list(map(int, keep))
        for i in keep:
            for j in dices:
                if i == j:
                    dices.remove(j)
                    break

        if len(keep) + len(dices) == 5:
            break
        else:
            print("This number doesn't exist")

    return keep



# newList = list(set(dices) - set(keep))
# print(newList)

# newList = dices
# for i in range(len(dices)-1):
#     for j in range(len(keep)-1):
#         if dices[i] == keep[j]:
#             newList.pop(i)

# newList = [ x for x in keep if not x in dices ]

# newList = lambda dices, keep: list(filter(lambda element: element not in dices, keep))
# newList = f(keep, dices)
# x = OrderedDict.fromkeys(dices)
# y = OrderedDict.fromkeys(keep)
#
# for k in x:
#     if k in y:
#         x.pop(k)
#         y.pop(k)
#
#
# print(x.keys())
# print(y.keys())
# print(newList)
# print(list(set(dices).intersection(set(keep))))

if __name__ == '__main__':
    main()