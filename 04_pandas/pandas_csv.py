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
# ------------------------------------------------------

# shape_statement = df.shape
# len_statement = shape_statement[0]
# print(type(len_statement))

# print(df['Open Time'].apply(lambda x: x.split(' ')[0] if len(x) > 10 else x))
day_statement = list(df['Open Time'].apply(lambda x: x.split(' ')[0] if len(x) > 10 else x))
cut_day_statement = list(set(day_statement))
cut_day_statement.sort(key = lambda date: datetime.strptime(date, '%Y.%m.%d'))

for i in range(len(cut_day_statement)):
    print(cut_day_statement[i])

day_n = '2021.06.12'
day_real = datetime.strptime(day_n, '%Y.%m.%d')
format_day = day_real.strftime('%A - %d %B %Y')
print(format_day)

num = 84.11999999999998
# short_num = '{0:.3g}'.format(num)
short_num = round(num, 2)
print(short_num)

# size_statements = list(df['Size'])
# print(size_statements)
# print(list(set(size_statements)))

