#!/usr/bin/env python3

import pandas as pd
from datetime import datetime


# df = pd.read_csv('survey/survey_results_public.csv')
# df = pd.read_csv('statements/statement.csv')
df = pd.read_excel('statements/statement.xlsx')

# -----------------------------------------------------
# print(df)           # data frame
# print(df.shape)
# print(df.info())
# print(df[['Open Time', 'Type', 'Size', 'Item', 'Profit']])
# print(df[['Open Time', 'Type', 'Size', 'Item', 'Profit']].head(4))
# print(df[:5]['Profit'])
# print(df.sort_values(by='Profit'))
# print(df.sort_values(by='Profit', ascending=False))
# print(df.Profit.sum())
# print(df['Profit'].min())       # Classic notation
# print(df.Profit.max())          # Panda notation
# print(df.Profit.mean())
# print(df[df.Profit > 500])
# print(df['Open Time'].str[:10])
# print(df[df['Open Time'].str[:10] == '2021.06.01'])
# print(df.columns)
# print(df.iloc[3])
# print(df.iloc[[3, 10]])                 # show 3 & 10 row
# print(df.iloc[[3, 10], [1, 2, 3, 13]])  # show [rows], [columns]
# print(df.loc[[3, 10], ['Profit', 'Size']])  # show [rows], [columns]
# print(df.loc[0:10, ['Profit', 'Size']])  # show [rows], [columns]
# print(df['Size'].value_counts())
# --- Index ---
# print(df.set_index('Profit'))                   # Temporary changes
# print(df.set_index('Profit', inplace=True))     # Permament changes
# print(df.set_index('Profit').sort_index(ascending=True))
# print(df.sort_index())
# --- Filtering ---
# print(df['Commission'] == -9.6)   # show 'True' or 'False' per column
# filt = (df['Commission'] == -9.6)
# print(df[filt])                     # return all row with 'True' criteria
# print(df.loc[filt])                 # --//--
# print(df.loc[filt, 'Profit'])       # --//-- , and show only this column
# filt = (df['Close Time'].str[:10] == '2021.06.08') & (df['Profit'] <= -100)
# print(df[filt])
# print(df[~filt])                    # show only opposite results
### this string is contains in 'Close Time' column
# filt = df['Close Time'].str.contains('2021.06.08', na=False)
# print(df[filt])
# --- Updating Rows and Columns ---
# df.columns = [x.upper() for x in df.columns]    # change to uppercase col name
# print(df)
# df.columns = df.columns.str.replace(' ', '_')   # replace 
# print(df.columns)
# df.rename(columns={'S / L': 'Stop Loss', 'T / P': 'Take Profit'}, inplace=True)
# print(df)
# df.loc[29, ['Type']] = ['sell'] # replace value in specific columns
# print(df)
### filtr and change value
# filt = (df['Commission'] == -9.6)
# df.loc[filt, 'Type'] = 'sell'
# print(df)
###
#print(df['Type'].apply(len))    # show length 
### change function
# def change_to_upper(text):
#     return text.upper()
# df['Type'] = df['Type'].apply(change_to_upper)
# print(df)
# df['Type'] = df['Type'].apply(lambda x: x.lower())  # Reverse changes
# print(df)
###
# print(df.applymap(len))
# ---Add/Remove Rows and Columns From DataFrames ---
# df['Ballance'] = df['Profit'] + df['Commission']    # add column (temporary)
# print(df)
# print(df.drop(columns=['Taxes', 'Swap']))   # drop columns (temporary)
# df.drop(columns=['Taxes', 'Swap'], inplace=True)   # drop columns (permanently)
# print(df)
# print(df['Open Time'].str.split(' '))   # make a list from 'Open Time' column
# print(df['Open Time'].str.split(' ', expand=True))   # split 'Open Time' column
# df[['Date', 'Time']] = df['Open Time'].str.split(' ', expand=True)
# print(df.drop(index=4))
filt = df['Commission'] == -9.6
print(df.drop(index=df[filt].index))
# print(df)




# ------------------------------------------------------
# --- Format Date. Cut Time from date ---
# df['Open Time'] = pd.to_datetime(df['Open Time']).dt.date
# df['Close Time'] = pd.to_datetime(df['Close Time']).dt.date
# print(df)
# print(df.info())

# format_days = []
# url_statements = list(set(df['Close Time']))
# url_statements.sort()
# url_statements['Close Time'] = pd.to_datetime(url_statements['Close Time']).dt.date
# for url_stat in url_statements:
    # format_days.append(url_stat.strftime('%A - %d %B %Y'))
    # day_st = df.loc[df['Close Time'] == url_stat]
    # short_date = pd.to_datetime(url_stat).date
    # print(url_stat)

# print(url_statements)
# print(format_days)
# print(day_st)

# --- Shape -> columns & rows ---
# shape_statement = df.shape
# len_statement = shape_statement[0]
# print(type(len_statement))

# --- Cut date day statement ---
# print(df['Open Time'].apply(lambda x: x.split(' ')[0] if len(x) > 10 else x))
# day_statement = list(df['Open Time'].apply(lambda x: x.split(' ')[0] if len(x) > 10 else x))
# cut_day_statement = list(set(day_statement))
# cut_day_statement.sort(key = lambda date: datetime.strptime(date, '%Y.%m.%d'))
# for i in range(len(cut_day_statement)):
#     print(cut_day_statement[i])

# --- Format Date ---
# day_n = '2021.06.12'
# day_real = datetime.strptime(day_n, '%Y.%m.%d')
# format_day = day_real.strftime('%A - %d %B %Y')
# print(format_day)

# --- Round numbers ---
# num = 84.11999999999998
# short_num = round(num, 2)
# print(short_num)

# --- Set Liste ---
# size_statements = list(df['Size'])
# print(size_statements)
# print(list(set(size_statements)))

# -- Balance ---
# balance = df.Profit.sum()
# print(balance)

# --- Count Profit ---
# sum_profit = 0
# for i in df.Profit:
#     if i > 0:
#         sum_profit += i
# print(sum_profit)

# --- pkt ---
# pkt_buy, pkt_sell = 0, 0
# for index, row in df.iterrows():
#     if row['Type'] == 'buy':
#         pkt_buy = (row['Price.1'] - row['Price'])
#     elif i['Type'] == 'sell':
#         pkt_sell = (row['Price'] - row['Price.1'])
#     pkt = (pkt_buy + pkt_sell)
#     print(round(pkt))

# ==============================================
#   Column      Non-Null Count  Dtype  
# ---  ------      --------------  -----  
# 0   Ticket      30 non-null     int64  
# 1   Open Time   30 non-null     object 
# 2   Type        30 non-null     object 
# 3   Size        30 non-null     float64
# 4   Item        30 non-null     object 
# 5   Price       30 non-null     float64
# 6   S / L       30 non-null     float64
# 7   T / P       30 non-null     float64
# 8   Close Time  30 non-null     object 
# 9   Price.1     30 non-null     float64
# 10  Commission  30 non-null     float64
# 11  Taxes       30 non-null     int64  
# 12  Swap        30 non-null     int64  
# 13  Profit      30 non-null     float64
# dtypes: float64(7), int64(3), object(4)
