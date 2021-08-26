from django.shortcuts import render
from django.views.generic import View
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Statement, Deposit
import pandas as pd
from datetime import datetime


def df_db():
    statements = Statement.objects.all().values()
    df = pd.DataFrame(statements)
    return df

def depo_db():
    deposits = Deposit.objects.all().values()
    depo = pd.DataFrame(deposits)
    return depo

def index(request):
    return render(request, 'cfd/index.html')


def deposit(request):
    depo = depo_db()
    depo = depo.drop(['id'], axis=1)
    depo['date_dep'] = pd.to_datetime(depo['date_dep']).dt.date
    context = {'depo': depo.to_html(index=False)}
    return render(request, 'cfd/deposit.html', context)


def withdrawal(request):
    return render(request, 'cfd/withdrawal.html')


def statement(request):
    df = df_db()
    all_sum = df.profit.sum()
    df['open_time'] = pd.to_datetime(df['open_time']).dt.date
    df['close_time'] = pd.to_datetime(df['close_time']).dt.date
    url_statements = list(set(df['close_time']))
    url_statements.sort()
    format_days = []
    profit = []
    loss = []
    balance = []
    for url_stat in url_statements:
        day_st = df.loc[df['close_time'] == url_stat]
        format_days.append(url_stat.strftime('%A - %d %B %Y'))

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
    day_st = df[df['close_time'].dt.strftime('%Y-%m-%d') == url_statement]
    df = df.drop(['id', 'ticket', 'taxes'], axis=1)
    day_st = day_st.drop(['id', 'ticket', 'taxes'], axis=1)
    day_real = datetime.strptime(url_statement, '%Y-%m-%d')
    format_day = day_real.strftime('%A - %d %B %Y')
    format_day_from_request = day_st
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
    day_st['open_time'] = pd.to_datetime(day_st['open_time']).dt.date
    day_st['close_time'] = pd.to_datetime(day_st['close_time']).dt.date
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
        day_st = df[df['close_time'].dt.strftime('%Y-%m-%d') == url_from_request]
        labels = day_st.index.values
        chartdata = list(day_st.profit)
        data = {
                "labels": labels,
                "chartLabel": chartLabel,
                "chartdata": chartdata,
            }
        return Response(data)
