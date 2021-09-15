#!/usr/bin/env python3

import pandas as pd
from sqlalchemy import create_engine


# --- Read data from Excel file ---
df = pd.read_excel('~/Documents/statement.xlsx')

# --- Rename columns name ---
df.rename(columns={
    'Ticket': 'ticket',
    'Open Time': 'open_time',
    'Type': 'type_st',
    'Size': 'size_st',
    'Item': 'item_st',
    'Price': 'open_price',
    'S / L': 's_l',
    'T / P': 't_p',
    'Close Time': 'close_time',
    'Price.1': 'close_price',
    'Commission': 'commission',
    'Taxes': 'taxes',
    'Swap': 'swap',
    'Profit': 'profit'
    }, inplace=True)

# print(df)
# print(df.info())
# --- Convert the column type from string to datetime format ---
df['open_time'] = pd.to_datetime(df['open_time'])
df['close_time'] = pd.to_datetime(df['close_time'])

# print(df)
# print(df.info())
# --- conect to SQL database ---
engine = create_engine('mysql+pymysql://nook17_nook17:Nook,1771@136.243.46.32:3306/nook17_statement')

# --- Write to database ---
df.to_sql(
        name='cfd_statement',
        con=engine,
        index=True,
        index_label='id',
        if_exists='append',
        # if_exists='replace',
        )
