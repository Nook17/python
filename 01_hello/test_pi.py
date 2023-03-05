#!/usr/bin/env python3

# import time

# LED = [1, 2, 3, 4, 5]

# while True:
#     for x in LED:
#         print(x)
#         time.sleep(.2)

mth = ['January', 'February', 'March', 'April', 'May', 'June', 'July',
    'August', 'September', 'October', 'November', 'December']
depo_month = 115000
percent_month = 1
wd_month = 10000

earning = []
savings = []
start_next_mth = []

earning.append(depo_month * pow(1 + (percent_month / 100), 22) - depo_month)
savings.append(earning[0] - wd_month)
start_next_mth.append(savings[0] + depo_month)

for i in range(13):
    i += 1
    earning.append(start_next_mth[i-1] * pow(1 + (percent_month / 100), 22) - start_next_mth[i-1])
    savings.append(earning[i] - wd_month)
    start_next_mth.append(start_next_mth[i-1] * pow(1 + (percent_month / 100), 22) - wd_month)

for i in range(12):
    print(int(earning[i]), int(savings[i]), int(start_next_mth[i]))