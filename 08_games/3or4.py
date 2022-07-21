#!/usr/bin/env python3
import random
from collections import Counter

dices= []

for i in range(5):
    d = random.randint(1, 6)
    dices.append(d)
# dices.sort()
print(dices)
print(set(dices))
print(len(set(dices)))

sameElement = dict(Counter(dices))
print(sameElement)
for value in sameElement.values():
    if value >= 3:
        print('3 of a kind')
    if value >= 4:
        print('4 of a kind')