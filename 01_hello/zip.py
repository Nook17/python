#!/usr/bin/env python3

l1 = ['date1', 'date2', 'date3']
l2 = [10, 20, 30]
l3 = ['nook', 'kojo', 'kama']
l4 = ['warsaw', 'olsztyn', 'hel']

list = list(zip(l2, l3, l4))
dict = dict(zip(l1, list))

print(dict)
#for key, value in dict.items():
#    print(f"{key}:{value}")

# for i in range(len(dict)):
#     print(f"{dict['date2'][i]}")

# for key in dict:
#     print(key)
#     for i in range(len(dict)):
#         print(f"-> {dict[key][i]}")

for dic_date, dic_items in dict.items():
    print(f"{dic_date} -> {dict[dic_date][0]} {dict[dic_date][1]} {dict[dic_date][2]}")

# print(dict['date2'][2])
