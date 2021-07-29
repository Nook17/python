#!/usr/bin/env python3

import calendar, os, random, json

# --- Calendar ---
nook=calendar.TextCalendar(calendar.MONDAY)
nook.prmonth(2021, 7)
print('\nDni przestępnych od 1980: ', calendar.leapdays(1980, 2021))
print('\n', calendar.prcal(2021))
cal_www = open('calendar.html', 'w')
cal_www.write(calendar.HTMLCalendar(calendar.MONDAY).formatyear(2021))
cal_www.close()

# --- OS Module ---
print(os.getcwd())
# os.system('qutebrowser')

# --- Random ---
print(random.randint(0, 6))
print(random.random() *100)

with open("alphabet_phonetic_NATO.txt", "r") as f:
    file_str = f.read()             # file_str -> type str
file_lst = file_str.split()         # file_lst -> type list
print(random.choice(file_lst))

random.shuffle(file_lst)            #shuffle list
print(file_lst)

for i in range(10):
    print(random.randrange(0, 200, 10))     # random using start - stop - step

print(' --- Random English Words ---')
wds = int(input('How many words shall I choose? : '))
with open('english-words/words_alpha.txt', 'rt') as f:
    words = f.readlines()
words = [w.rstrip() for w in words]
for w in random.sample(words, wds):
    print(w)
