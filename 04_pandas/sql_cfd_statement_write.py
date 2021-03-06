#!/usr/bin/env python3

import pandas as pd
from sqlalchemy import create_engine

# --- conect to SQL database ---
engine = create_engine('mysql+pymysql://root@localhost:3306/statement')

# --- Write to database ---
df = pd.read_excel('statements/statement_long.xlsx')
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

df[["open_time", "close_time"]] = df[["open_time", "close_time"]].apply(pd.to_datetime)

df.to_sql(
        name='cfd_statement',
        con=engine,
        index=True,
        index_label='id',
        # if_exists='append',
        if_exists='replace',
        )
