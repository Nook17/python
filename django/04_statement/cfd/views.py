from django.shortcuts import render, redirect
from django.views.generic import View
from django.http import HttpResponseRedirect
from django.urls import reverse
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Statement, Deposit, Withdrawal, Notesdb, Buy_calc
from .forms import DepositForm, WithdrawalForm, NotesdbForm, Buy_calcForm
import pandas as pd
import json
from datetime import datetime


def df_db():
    statements = Statement.objects.all().values()
    df = pd.DataFrame(statements)
    return df


def depo_db():
    deposits = Deposit.objects.all().values().order_by('date_dep')
    return deposits


def depo_db_pandas():
    deposits = Deposit.objects.all().values()
    depo = pd.DataFrame(deposits)
    return depo


def wd_db():
    withdrawal = Withdrawal.objects.all().values().order_by('date_wd')
    return withdrawal


def wd_db_pandas():
    withdrawal = Withdrawal.objects.all().values()
    wd = pd.DataFrame(withdrawal)
    return wd


def index(request):
    return render(request, 'cfd/index.html')


def deposit(request):
    depo = depo_db()
    depo_sum = depo_db_pandas()
    if not depo_sum.empty:
        sum = depo_sum.amount_dep.sum()
    else:
        sum = 0
    context = {'depo': depo, 'sum': sum}
    return render(request, 'cfd/deposit.html', context)


def new_deposit(request):
    if request.method != 'POST':    # if 'GET'
        form = DepositForm()
    else:
        form = DepositForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('cfd:deposit')
    context = {'form': form}
    return render(request, 'cfd/new_deposit.html', context)


def update_deposit(request, deposit_id):
    updepo = Deposit.objects.get(id=deposit_id)
    if request.method != 'POST':
        form = DepositForm(instance=updepo)
    else:
        form = DepositForm(instance=updepo, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('cfd:deposit')
    context = {'updepo': updepo, 'form': form}
    return render(request, 'cfd/update_deposit.html', context)


def delete_deposit(request, deposit_id):
    depo = depo_db()
    try:
        deldepo = Deposit.objects.get(id=deposit_id)
    except Deposit.DoesNotExist:
        return redirect('cfd:deposit')
    deldepo.delete()
    context = {'depo': depo}
    return HttpResponseRedirect(reverse('cfd:deposit'))
    return render(request, 'cfd/deposit.html', context)


def withdrawal(request):
    wdd = wd_db()
    wd_sum = wd_db_pandas()
    if not wd_sum.empty:
        sum = wd_sum.amount_wd.sum()
    else:
        sum = 0
    context = {'wdd': wdd, 'sum': sum}
    return render(request, 'cfd/withdrawal.html', context)


def new_withdrawal(request):
    if request.method != 'POST':    # if 'GET'
        form = WithdrawalForm()
    else:
        form = WithdrawalForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('cfd:withdrawal')
    context = {'form': form}
    return render(request, 'cfd/new_withdrawal.html', context)


def update_withdrawal(request, withdrawal_id):
    upwd = Withdrawal.objects.get(id=withdrawal_id)
    if request.method != 'POST':
        form = WithdrawalForm(instance=upwd)
    else:
        form = WithdrawalForm(instance=upwd, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('cfd:withdrawal')
    context = {'upwd': upwd, 'form': form}
    return render(request, 'cfd/update_withdrawal.html', context)


def delete_withdrawal(request, withdrawal_id):
    wdd = wd_db()
    try:
        delwd = Withdrawal.objects.get(id=withdrawal_id)
    except Withdrawal.DoesNotExist:
        return redirect('cfd:withdrawal')
    delwd.delete()
    context = {'wdd': wdd}
    return HttpResponseRedirect(reverse('cfd:withdrawal'))
    return render(request, 'cfd/withdrawal.html', context)


def statement(request):
    df = df_db()
    commission_sum = df.commission.sum()
    swap_sum = df.swap.sum()
    filter_profit = (df['profit'] > 0)
    filter_loss = (df['profit'] < 0)
    profit_sum = df.loc[filter_profit, 'profit'].sum()
    loss_sum = df.loc[filter_loss, 'profit'].sum()
    ballance_sum = profit_sum + loss_sum + commission_sum + swap_sum
    df['open_time'] = pd.to_datetime(df['open_time']).dt.date
    df['close_time'] = pd.to_datetime(df['close_time']).dt.date
    url_statements = list(set(df['close_time']))
    url_statements.sort()
    format_days = []
    profit_per_day = []
    loss_per_day = []
    balance_per_day = []
    for url_stat in url_statements:
        day_st = df.loc[df['close_time'] == url_stat]
        format_days.append(url_stat.strftime('%A - %d %B %Y'))
        # --- commision ---
        commission_day = day_st.commission.sum()
        # --- Profit ----
        sum_profit = 0
        for i in day_st.profit:
            if i > 0:
                sum_profit += i
        profit_per_day.append(sum_profit + commission_day)
        # --- Loss ---
        loss_profit = 0
        for i in day_st.profit:
            if i < 0:
                loss_profit += i
        loss_per_day.append(loss_profit)
        # --- Balance ---
        day_sum = sum_profit + commission_day + loss_profit
        balance_per_day.append(day_sum)
    lists = list(zip(format_days, profit_per_day, loss_per_day, balance_per_day))
    dicts = dict(zip(url_statements, lists))
    context = {'dicts': dicts,
               'profit_sum': round(profit_sum, 2),
               'loss_sum': round(loss_sum, 2),
               'ballance_sum': round(ballance_sum, 2),
               'commission_sum': round(commission_sum, 2),
               'swap_sum': round(swap_sum, 2)}
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


def year(request):
    per = Notesdb.objects.all().values()
    df = pd.DataFrame(per)
    if not len(df.columns) == 0:
        filt = (df['id'] == 1)
        percent = float(df.loc[filt, 'percent_year'])
        amount_base = int(df.loc[filt, 'amount_year'])
    else:
        percent = 1
        amount_base = 1000
    l1, l2, l3, lper, lsum = [], [], [], [], []
    amount = amount_base
    for i in range(264):
        l1.append(amount)
        numb = (amount * percent) / 100
        amount += numb
        l2.append(numb)
        l3.append(amount)
        lper.append(((amount - amount_base) / amount_base) * 100)
    for i in range(1, 13):
        lsum.append(l3[(i*22)-1] - l1[(i*22)-22])
    lists = list(zip(l1, l2, l3, lper))
    context = {'percent': percent, 'amount_base': amount_base, 'lists': lists,
               'lsum': lsum}
    return render(request, 'cfd/year.html', context)


def new_percent(request):
    per = Notesdb.objects.all().values()
    df = pd.DataFrame(per)
    if not df.empty:
        n_per = Notesdb.objects.get(id=1)
        if request.method != 'POST':
            form = NotesdbForm(instance=n_per)
        else:
            form = NotesdbForm(instance=n_per, data=request.POST)
            if form.is_valid():
                form.save()
                return redirect('cfd:year')
        return redirect('cfd:year')
    else:
        form = NotesdbForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('cfd:year')
    return redirect('cfd:year')


def calc(request):
    cal = Notesdb.objects.all().values()
    buy_level = Buy_calc.objects.all().values().order_by('-buy_level')
    df_cal = pd.DataFrame(cal)
    # df_buy = pd.DataFrame(buy_lev)
    # buy_level = list(set(df_buy['buy_level']))
    if not len(df_cal.columns) == 0:
        filt = (df_cal['id'] == 2)
        gap = int(df_cal.loc[filt, 'gap'])
        lot = float(df_cal.loc[filt, 'lot'])
        margin_value = int(df_cal.loc[filt, 'margin_value'])
        pip_value = float(df_cal.loc[filt, 'pip_value'])
        tp_buy = int(df_cal.loc[filt, 'tp_buy'])
    else:
        percent = 1
        amount_base = 1000
    context = {'gap': gap, 'lot': lot, 'margin_value': margin_value,
               'pip_value': pip_value, 'tp_buy': tp_buy,
               'buy_level': buy_level}    
    return render(request, 'cfd/calc.html', context)


def calc_set(request):
    cal = Notesdb.objects.all().values()
    df = pd.DataFrame(cal)
    if not df.empty:
        cal_db = Notesdb.objects.get(id=2)
        if request.method != 'POST':
            form = NotesdbForm(instance=cal_db)
        else:
            form = NotesdbForm(instance=cal_db, data=request.POST)
            if form.is_valid():
                form.save()
                return redirect('cfd:calc')
        return redirect('cfd:calc')
    else:
        form = NotesdbForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('cfd:calc')
    return render(request, 'cfd/calc.html')


def calc_buy_create(request):
    if request.method != 'POST':
        form = Buy_calcForm()
    else:
        form = Buy_calcForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('cfd:calc')    
    return render(request, 'cfd/calc.html')


# def calc_buy_update(request, buy_id):
    # upwd = Withdrawal.objects.get(id=withdrawal_id)
    # if request.method != 'POST':
    #     form = WithdrawalForm(instance=upwd)
    # else:
    #     form = WithdrawalForm(instance=upwd, data=request.POST)
    #     if form.is_valid():
    #         form.save()
    #         return redirect('cfd:withdrawal')    
    # return render(request, 'cfd/calc.html')


def calc_buy_delete(request, buy_id):
    # cbd = Buy_calc.objects.all().values()
    try:
        cbd = Buy_calc.objects.get(id=buy_id)
    except Buy_calc.DoesNotExist:
        return redirect('cfd:calc')
    cbd.delete()
    return HttpResponseRedirect(reverse('cfd:calc'))    
