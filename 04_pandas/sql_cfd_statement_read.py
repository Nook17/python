#!/usr/bin/env python3

import pandas as pd
from sqlalchemy import create_engine

# --- conect to SQL database ---
engine = create_engine('mysql+pymysql://root@localhost:3306/statement')

# --- read from database ---
# df = pd.read_sql_table("cfd_statement", engine)
df = pd.read_sql("cfd_statement", engine)
# df = pd.read_sql("cfd_quarter", engine)
# print(df.shape[0])
# print(df.info())
# print(df.loc[0:10, ['Profit', 'Size']])

url_statement = '2021-09-14'
day_st = df[df['close_time'].dt.strftime('%Y-%m-%d') == url_statement]
# df = df.drop(['id', 'ticket', 'taxes'], axis=1)
day_st = day_st.drop(['id', 'ticket', 'taxes'], axis=1)
# day_real = datetime.strptime(url_statement, '%Y-%m-%d')
# format_day = day_real.strftime('%A - %d %B %Y')
# format_day_from_request = day_st
# # --- commision ---
# commission_sum = day_st.commission.sum()
# # --- Profit ----
# sum_profit = 0
# for i in day_st.profit:
#     if i > 0:
#         sum_profit += i
# sum_profit += commission_sum
# # --- Loss ---
# loss_profit = 0
# for i in day_st.profit:
#     if i < 0:
#         loss_profit += i
# # --- Balance ---
# day_sum = sum_profit + loss_profit
# # --- pkt ---
# pkt_buy, pkt_sell = 0, 0
# for index, row in day_st.iterrows():
#     if row['type_st'] == 'buy':
#         pkt_buy += (row['close_price'] - row['open_price'])
#     elif row['type_st'] == 'sell':
#         pkt_sell += (row['open_price'] - row['close_price'])
# pkt_sum = pkt_buy + pkt_sell
# --- Swap ---
# swap_sum = day_st.swap.sum()
# -------------------
day_st['open_time'] = pd.to_datetime(day_st['open_time']).dt.date
day_st['close_time'] = pd.to_datetime(day_st['close_time']).dt.date
day_st.rename(columns={
    'ticket': 'Ticket',
    'open_time': 'Open Time',
    'type_st': 'Type',
    'size_st': 'Size',
    'item_st': 'Item',
    'open_price': 'Open Price',
    's_l': 'Stop Loss',
    't_p': 'Take Profit',
    'close_time': 'Close Time',
    'close_price': 'Close Price',
    'commission': 'Commission',
    'taxes': 'Taxes',
    'swap': 'Swap',
    'profit': 'Profit'
    }, inplace=True)

for i, day in day_st.iterrows():
    print(i, day['Profit'])


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
