#!/usr/bin/env python3

import pandas as pd
from sqlalchemy import create_engine

# --- Read data from Excel file ---
df = pd.read_excel('statements/deposit.xlsx')

# --- Convert the column type from string to datetime format ---
df['date_dep'] = pd.to_datetime(df['date_dep'])

# --- conect to SQL database ---
engine = create_engine('mysql+pymysql://root@localhost:3306/statement')

# --- Write to database ---
df.to_sql(
        name='cfd_deposit',
        con=engine,
        index=True,
        index_label='id',
        # if_exists='append',
        if_exists='replace',
        )
