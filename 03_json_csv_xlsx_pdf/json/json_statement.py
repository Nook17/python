#!/usr/bin/env python3

import matplotlib.pyplot as plt
import json

json_nook = '''
{
  "Sheet": [
    {
      "Ticket": 107843118,
      "Open Time": "2021.05.31 15:29:44",
      "Type": "buy",
      "Size": 0.3,
      "Item": "us.100..",
      "Price": 13680.77,
      "T / P": 13680.77,
      "Close Time": "2021.06.01 00:26:26",
      "Commission": -19.6,
      "Profit": 54.86
    },
    {
      "Ticket": 107846543,
      "Open Time": "2021.06.01 07:51:28",
      "Type": "buy",
      "Size": 0.3,
      "Item": "us.100..",
      "Price": 13694.72,
      "T / P": 13694.72,
      "Close Time": "2021.06.01 08:03:53",
      "Commission": -2.6,
      "Profit": 165.91
    },
    {
      "Ticket": 107846653,
      "Open Time": "2021.06.01 08:10:59",
      "Type": "buy",
      "Size": 0.3,
      "Item": "us.100..",
      "Price": 13691.53,
      "T / P": 13691.53,
      "Close Time": "2021.06.01 08:14:40",
      "Commission": -9.6,
      "Profit": 25.98
    }
  ]
}
'''

# --- local variable ---
# data = json.loads(json_nook)
# for money in data['Sheet']:
#     print(money['Profit'])

# data = json.loads(json_nook)
# new_data = json.dumps(data, indent=2)
# print(new_data)

# --- load file ---
# j = open('statement_short.json', 'r')
# statements = json.load(j)
# print(statements)

profit = []

with open('statement_long.json', 'r') as j:
    statement = json.load(j)
for sheet in statement['Sheet1']:
    profit.append(float(sheet['Profit']))
    print(sheet['Profit'])

fig, ax = plt.subplots()
ax.plot(profit)
plt.show()
