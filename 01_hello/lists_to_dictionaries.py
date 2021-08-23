#!/usr/bin/env python3

list1 = [
        '2021.07.09',
        '2021.07.12',
        '2021.07.13',
        '2021.07.15',
        '2021.07.16',
        '2021.07.19',
        '2021.07.20'
        ]

list2 = [
        'date1',
        'date2',
        'date3',
        'date4',
        'date5',
        'date6',
        'date7'
        ]

dict = {}
dict = {list1[i]: list2[i] for i in range(len(list1))}

print(dict)

for key, value in dict.items():
    print(f"{key} -> {value}")
