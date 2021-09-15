#!/usr/bin/env python3

import pandas as pd
from sqlalchemy import create_engine

# --- conect to SQL database ---
engine = create_engine('mysql+pymysql://root@localhost:3306/statement')

# --- read from database ---
df = pd.read_sql("cfd_quarter", engine)
# print(df)
# print(df.info())
# filt = df['id'] == 1
# print(df.loc[filt, 'profit'])
# qrt_row_number = df.shape[0]
# lprof = []
# for i in range(6):
#     if qrt_row_number > i:
#         lprof.append(int(df.loc[df['id'] == i+1, 'profit']))

# print(lprof)

df['date'] = pd.to_datetime(df['date']).dt.date
dtd = df['date'].tolist()
ldate = []
for url_stat in dtd:
    ldate.append(url_stat.strftime('%d-%b'))

for i in range(6):
    if i >= len(ldate):
        ldate.append(0)
print(ldate)

# -- last value ---
print(df['id'].iloc[-1])

# print(df.loc[0:10, ['Profit', 'Size']])
# --- Format Date. Cut Time from date ---
# df['open_time'] = pd.to_datetime(df['open_time']).dt.date
# df['close_time'] = pd.to_datetime(df['close_time']).dt.date
# print(df)

# format_days = []
# url_statements = list(set(df['close_time']))
# url_statements.sort()
# for url_stat in url_statements:
#     format_days.append(url_stat.strftime('%A - %d %B %Y'))
#     day_st = df.loc[df['close_time'] == url_stat]
# day_st = df[df['close_time'].dt.strftime('%Y-%m-%d') == '2021-08-19']
# day_st = df[df['close_time'] == '2021-07-12']
# day_st = df.query("close_time = '2021-07-12'")
# print(day_st)
# print(df)

# --- Write to database ---
# df = pd.read_excel('statements/statement.xlsx')
# df.rename(columns={
#     'Ticket': 'ticket',
#     'Open Time': 'open_time',
#     'Type': 'type_st',
#     'Size': 'size_st',
#     'Item': 'item_st',
#     'Price': 'open_price',
#     'S / L': 's_l',
#     'T / P': 't_p',
#     'Close Time': 'close_time',
#     'Price.1': 'close_price',
#     'Commission': 'commission',
#     'Taxes': 'taxes',
#     'Swap': 'swap',
#     'Profit': 'profit'
#     }, inplace=True)
# df.to_sql(
#         name='cfd_statement',
#         con=engine,
#         index=False,
#         if_exists='append'
#         )