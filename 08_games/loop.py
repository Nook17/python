#!/usr/bin/env python3
import random


dice = [1, 1, 6, 6, 6]
print(dice)
for i in range(1, 7):
    print('i - {}'.format(i))
    if dice.count(i) == 3:
        for j in range(1, 7):
            print('j - {}'.format(j))
            if j != i:
                if dice.count(j) == 2:
                    print('full')
