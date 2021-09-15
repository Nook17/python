#!/usr/bin/env python3

import pandas as pd
# import mysql.connector
from sqlalchemy import create_engine

# --- conect to SQL database -> create_engine ---
engine = create_engine('mysql+pymysql://nook17_nook17:Nook,1771@136.243.46.32:3306/nook17_statement')

# --- conect to SQL database -> mysql.connector.connect ---
# engine = mysql.connector.connect(
#       host="136.243.46.32",
#       user="nook17_nook17",
#       passwd="Nook,1771",
#       database="nook17_statement"
#     )

# --- SQL Query ---
# sql = 'SELECT * from cfd_notesdb'

# -------- Read from database --------
df = pd.read_sql_table("cfd_statement", engine)
# df = pd.read_sql("cfd_notesdb", engine)
# df = pd.read_sql(sql, engine)

# --------------------------------------------
# print(df)
# print(df.info())
# filt = (df['id'] == 2)
# select = df.loc[filt, 'buy_or_sell']
# print(select)

# --- Access a Single Value ---
# value = df.at[2, 'amount_quarter']
# value = df.iat[2, 10]

print(df)

