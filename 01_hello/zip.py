#!/usr/bin/env python3

l1 = ['date1', 'date2', 'date3']
l2 = [10, 20, 30]
l3 = ['nook', 'kojo', 'kama']
l4 = ['warsaw', 'olsztyn', 'hel']
l5 = ['laptop', 'pc', 'tel']

lists = list(zip(l2, l3, l4, l5))
dicts = dict(zip(l1, lists))

print(dicts)
#for key, value in dict.items():
#    print(f"{key}:{value}")

# for i in range(len(dict)):
#     print(f"{dict['date2'][i]}")

# for key in dict:
#     print(key)
#     for i in range(len(dict)):
#         print(f"-> {dict[key][i]}")

for dic_date, dic_items in dicts.items():
    # print(f"{dic_date} -> {dicts[dic_date][0]} {dicts[dic_date][1]} {dicts[dic_date][2]} {dicts[dic_date][3]}")
    print(f"{dic_date} -> {dic_items[0]} {dic_items[1]} {dic_items[2]} {dic_items[3]}")

# print(dict['date2'][2])
