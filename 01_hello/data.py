#!/usr/bin/env python3

import time

start_time = time.time()

# --- Lists ---
kojoi = []
kojoj = [3, 54, 23, 22, 37, 15, 45]     # type List
kojos = ['mama', 'tata', 'dziadek']

print(kojos[1], 'ma', kojoj[2], 'lat')
print(kojoj[1:3])
kojos += ['babcia']
sum_list = kojoj + kojos    # join List
print(sum_list)
kojos.append('ciocia')      # append element to end list
print(kojos[-1])            # show last element
del kojos[-1]               # removal item
print(kojos[-1])
kojos.remove('mama')
print(kojos[0])
kojoj.insert(4, 100)        # insert value 100 in 4'th place
print(kojoj)
kojoj.pop(4)                # remove the 4'th item from the list
print(kojoj)
print(kojos)

multiple_list = [('kojo', 10), ('mama', 46), ('kamila', 12), ('tata', 40), ('szczur', 0), ('kot', 13)]      # type list
for i in range(len(multiple_list)): 
    print(multiple_list[i][0], 'ma', multiple_list[i][1], 'lat')

print('Max No.:', max(kojoj))
print('Min No.:', min(kojoj))

# --- Dictionaries --- Key:Value
print("\n-------------------- Dictionaries ---------------------------")
factory = {         
        'opel': 1920,
        'VW': 1854,                 # type Dictionery
        'Mercedes': 1905,
        'Toyota': 1978
        }
print(factory)
print(factory['opel'])
factory['Suzuki'] = 1900
print(factory)
del factory['Suzuki']
print(factory)
car = input('Enter car name: ')
date_production = int(input('Enter date production: '))
factory[car] = date_production
print(factory.get('Honda', "\033[91mYou can't have this car in Dictionery\033[0m"))
for i in factory.items():       # .values()  .keys()
    print(i)
print("-------------------- END Dictionaries ------------------------\n")

# --- Splitting & Joining Strings ---
text = "Według Biura Analiz Makroekonomicznych Banku Millenium"
tables = text.split(' ')            # Split the content by 'space'
print(tables)
text = "US100,US500,DE30,RUSSEL,BITCOIN"
tables = text.split(',')            # Split the content by ','
print(tables)
list = ["Według", "Biura", "Analiz", "Makroekonomicznych", "Banku", "Millenium"]
text = " ".join(list)
print(text.lower())

# --- Formatin Strings ---
print("Dawno temu {} i {} poszli do lasu a {} w tym czasie robiła na drutach".format(kojos[0], kojos[1], kojos[2]))
numbers = (1, 4, 12, 34, 54)          # type Tuple
print('Some numbers: {}, {}, {}, {}'.format(*numbers))
print('Nubmers: {2}, {0}, {4}'.format(*numbers))

# --- Time & Date ---
print("Today is :\n", "\033[94m", time.strftime("%d %B %Y, %A - %H:%M"), "\033[0m")
print("Auto Time:\n", "\033[92m", time.asctime(), "\033[0m")
end_time = time.time() - start_time
print('Time to start program is:', "\033[91m", round(end_time, 2), "\033[0ms")

print=input("\n\033[41mPress Enter to Exit\033[0m")
