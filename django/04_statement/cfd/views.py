from django.shortcuts import render
from django.views.generic import View
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Statement
import pandas as pd
from datetime import datetime


def df_db():
    statements = Statement.objects.all().values()
    df = pd.DataFrame(statements)
    return df


def index(request):
    return render(request, 'cfd/index.html')


def statement(request):
    df = df_db()
    all_sum = df.profit.sum()
    day_statement = list(df['close_time'].apply(lambda x: x.split(' ')[0] if len(x)>10 else x))
    url_statements = list(set(day_statement))
    url_statements.sort(key=lambda date: datetime.strptime(date, '%Y.%m.%d'))
    format_days=[]
    profit=[]
    loss=[]
    balance=[]
    for url_stat in url_statements:
        day_real = datetime.strptime(url_stat, '%Y.%m.%d')
        format_days.append(day_real.strftime('%A - %d %B %Y'))

        day_st = df[df['close_time'].str[:10] == url_stat]
        # --- commision ---
        commission_sum = day_st.commission.sum()
        # --- Profit ----
        sum_profit = 0
        for i in day_st.profit:
            if i > 0:
                sum_profit += i
        profit.append(sum_profit + commission_sum)
        # --- Loss ---
        loss_profit = 0
        for i in day_st.profit:
            if i < 0:
                loss_profit += i
        loss.append(loss_profit)
        # --- Balance ---
        day_sum = sum_profit + commission_sum + loss_profit
        balance.append(day_sum)

    lists = list(zip(format_days, profit, loss, balance))
    dicts = dict(zip(url_statements, lists))

    context = {'all_sum': round(all_sum, 2), 'dicts': dicts}
    return render(request, 'cfd/statement.html', context)


url_from_request = ''
format_day_from_request = ''


def statements(request, url_statement):
    df = df_db()
    global url_from_request
    global format_day_from_request
    url_from_request = url_statement
    day_st = df[df['close_time'].str[:10] == url_statement]
    day_st = day_st.drop(['id', 'ticket', 'taxes'], axis=1)
    day_real = datetime.strptime(url_statement, '%Y.%m.%d')
    format_day = day_real.strftime('%A - %d %B %Y')
    format_day_from_request = format_day
    # --- commision ---
    commission_sum = day_st.commission.sum()
    # --- Profit ----
    sum_profit = 0
    for i in day_st.profit:
        if i > 0:
            sum_profit += i
    sum_profit += commission_sum
    # --- Loss ---
    loss_profit = 0
    for i in day_st.profit:
        if i < 0:
            loss_profit += i
    # --- Balance ---
    day_sum = sum_profit + loss_profit
    # --- pkt ---
    pkt_buy, pkt_sell = 0, 0
    for index, row in day_st.iterrows():
        if row['type_st'] == 'buy':
            pkt_buy += (row['close_price'] - row['open_price'])
        elif row['type_st'] == 'sell':
            pkt_sell += (row['open_price'] - row['close_price'])
    pkt_sum = pkt_buy + pkt_sell
    # --- Swap ---
    swap_sum = day_st.swap.sum()
    # -------------------
    context = {
            'format_day': format_day, 'day_st': day_st.to_html(index=False),
            'day_sum': round(day_sum, 2), 'sum_profit': round(sum_profit, 2),
            'loss_profit': round(loss_profit, 2), 'pkt_sum': round(pkt_sum, 2),
            'commission_sum': round(commission_sum, 2), 
            'swap_sum': round(swap_sum, 2), 'url_from_request': url_from_request}
    return render(request, 'cfd/statements.html', context)


class ChartData(APIView):
    # authentication_classes = []
    # permission_classes = []

    def get(self, request, format=None):
        global url_from_request
        global format_day_from_request
        chartLabel = format_day_from_request
        df = df_db()
        day_st = df[df['close_time'].str[:10] == url_from_request]
        labels = day_st.index.values
        chartdata = list(day_st.profit)
        data = {
                "labels": labels,
                "chartLabel": chartLabel,
                "chartdata": chartdata,
            }
        return Response(data)