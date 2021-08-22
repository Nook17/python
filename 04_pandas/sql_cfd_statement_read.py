#!/usr/bin/env python3

import pandas as pd
from sqlalchemy import create_engine

# --- conect to SQL database ---
engine = create_engine('mysql+pymysql://root@localhost:3306/statement')

# --- read from database ---
df = pd.read_sql_table("cfd_statement", engine)
print(df)
print(df.info())
# print(df.loc[0:10, ['Profit', 'Size']])  

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
