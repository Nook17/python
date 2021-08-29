#!/usr/bin/env python3

lm = ['MONTH 1', 'MONTH 2', 'MONTH 3', 'MONTH 4', 'MONTH 5', 'MONTH 6', 'MONTH 7', 'MONTH 8', 'MONTH 9', 'MONTH 10', 'MONTH 11', 'MONTH 12']
l1 = []
l2 = []
l3 = []
l4 = []

amount = 7000
percent_year = 1

for i in range(264):
    l1.append(amount)
    numb = (amount * percent_year) / 100
    amount += numb
    l2.append(numb)
    l3.append(amount)

# print(l1)
# print(l2)
# print(l3)

for i in range(22):
    print(f"{round(l1[i])} -> {round(l2[i])} -> {round(l3[i])}")

# lists = list(zip(l1, l2, l3))
# dicts = dict(zip('Month 1', lists))

# print(lists)

# print(dicts)
#for key, value in dict.items():
#    print(f"{key}:{value}")

# for i in range(len(dict)):
#     print(f"{dict['date2'][i]}")

# for key in dict:
#     print(key)
#     for i in range(len(dict)):
#         print(f"-> {dict[key][i]}")

# for dic_date, dic_items in dicts.items():
    # print(f"{dic_date} -> {dicts[dic_date][0]} {dicts[dic_date][1]} {dicts[dic_date][2]} {dicts[dic_date][3]}")
    # print(f"{dic_date} -> {dic_items[0]} {dic_items[1]} {dic_items[2]} {dic_items[3]}")

# print(dict['date2'][2])
