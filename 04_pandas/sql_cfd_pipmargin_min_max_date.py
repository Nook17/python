#!/usr/bin/env python3

import pandas as pd
from sqlalchemy import create_engine

# --- conect to SQL database ---
engine = create_engine('mysql+pymysql://root@localhost:3306/statement')

# --- read from database ---
# df = pd.read_sql_table("cfd_statement", engine)
# df = pd.read_sql("cfd_statement", engine)
df = pd.read_sql("cfd_pipmargin", engine)
# print(df.shape[0])
# print(df.info())
print(df)
# print(df.loc[0:10, ['Profit', 'Size']])

# --- MIN MAX Date ---
# df['updated_at'] = pd.to_datetime(df['updated_at'],format='%d/%m/%Y')
# last_market = df['market'].iloc[-1]
# last_pip = df['pip'].iloc[-1]
# filt = df['updated_at'].min()
# filt = max(df['updated_at'])
last_market = df.resample('D', on='updated_at')['market'].max()
last_margin = df.resample('D', on='updated_at')['margin'].max()
# print(df.loc[filt])
# print(last_margin)
# print(filt)
# print(df)
mark = list(last_market)
marg = int(last_margin)
mark_val = ''
for m in mark:
    mark_val = m
print(marg, mark_val) 
# print(mark)
# print(mark_val)
    

# --- som columns by date ---
# s = df.resample('M', on='close_time')['profit'].sum()
# s = df.resample('D', on='close_time')['profit'].sum()
# s = df.groupby(pd.Grouper(key='close_time', axis=0, freq='D')).sum()
# s = df.groupby(pd.Grouper(key='close_time', axis=0, freq='W', sort=True)).sum()
# s = drange=pd.date_range(df.close_time.min(),df.close_time.max())    
# s = df[(df['close_time'] >= '2021-08-20') & (df['close_time'] <= '2021-08-26 23:00:00')]['profit'].sum()
# s = df[(df['close_time'] <= '2021-08-26 23:00:00')]['profit'].sum()
# s = df['close_time'].dt.date.nunique()
# print(s)


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
