from django.shortcuts import render, redirect
from django.views.generic import View
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Statement, Deposit, Withdrawal, Notesdb, Buy_calc, Quarter, Pipmargin
from .forms import DepositForm, WithdrawalForm, NotesdbForm, Buy_calcForm, QuarterForm, PipmarginForm
import pandas as pd
import json, time
from datetime import datetime
from sqlalchemy import create_engine


def df_db():
    statements = Statement.objects.all().values()
    df = pd.DataFrame(statements)
    return df

def stat_db():
    statement = Statement.objects.all().values()
    return statement


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


def pipmargin_db_pandas():
    pipmarg = Pipmargin.objects.all().values()
    pm = pd.DataFrame(pipmarg)
    return pm


def deposit_sum():
    depo_sum = depo_db_pandas()
    if not depo_sum.empty:
        deposit_sum = depo_sum.amount_dep.sum()
    else:
        deposit_sum = 0
    return deposit_sum


def withdrawal_sum():
    wd_sum = wd_db_pandas()
    if not wd_sum.empty:
        withdrawal_sum = wd_sum.amount_wd.sum()
    else:
        withdrawal_sum = 0
    return withdrawal_sum


def wallet():
    df = df_db()
    commission_sum = df.commission.sum()
    swap_sum = df.swap.sum()
    filter_profit = (df['profit'] > 0)
    filter_loss = (df['profit'] < 0)
    profit = df.loc[filter_profit, 'profit'].sum()
    loss_sum = df.loc[filter_loss, 'profit'].sum()
    profit_sum = profit + loss_sum + commission_sum + swap_sum
    wall = profit_sum + deposit_sum()
    return wall


def days_count():
    df = df_db()
    return df['close_time'].dt.date.nunique()


def transactions():
    df = df_db()
    return df.shape[0]


def f_stat():
    df = df_db()
    depo_sum = deposit_sum()
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
    format_days, profit_per_day, loss_per_day, balance_per_day = [], [], [], [] 
    swap_day, wallet = [], []
    for url_stat in url_statements:
        day_st = df.loc[df['close_time'] == url_stat]
        format_days.append(url_stat.strftime('%A - %d %B %Y'))
        # --- commision ---
        commission_day = day_st.commission.sum()
        swap_day.append(day_st.swap.sum())
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
        # --- Sum Profit & Amount ---
        wallet.append(depo_sum + sum(balance_per_day) + sum(swap_day))
    lists = list(zip(format_days, profit_per_day, loss_per_day,
            balance_per_day, wallet))
    dicts = dict(zip(url_statements, lists))
    context = {'dicts': dicts,
               'profit_sum': round(profit_sum, 2),
               'loss_sum': round(loss_sum, 2),
               'ballance_sum': round(ballance_sum, 2),
               'commission_sum': round(commission_sum, 2),
               'swap_sum': round(swap_sum, 2)}
    return context


def f_stats(url_statement):
    df = df_db()
    day_st = df[df['close_time'].dt.strftime('%Y-%m-%d') == url_statement]
    df = df.drop(['id', 'ticket', 'taxes'], axis=1)
    day_st = day_st.drop(['id', 'taxes'], axis=1)
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
    # --- Data to chart ---
    day_ste = df[df['close_time'].dt.strftime('%Y-%m-%d') == url_statement]
    chartx = list(day_ste.index.values)
    charty = list(day_ste.profit)
    day_st.rename(columns={
        'ticket': 'Ticket',
        'open_time': 'Open Time',
        'type_st': 'Type',
        'size_st': 'Size',
        'item_st': 'Item',
        'open_price': 'Open Price',
        's_l': 'Stop Loss',
        't_p': 'Take Profit',
        'close_time': 'Close Time',
        'close_price': 'Close Price',
        'commission': 'Commission',
        'taxes': 'Taxes',
        'swap': 'Swap',
        'profit': 'Profit'
        }, inplace=True)
    context = {
            'format_day': format_day, 'chartx': chartx, 'charty': charty,
            'day_sum': round(day_sum, 2), 'sum_profit': round(sum_profit, 2),
            'loss_profit': round(loss_profit, 2), 'pkt_sum': round(pkt_sum, 2),
            'commission_sum': round(commission_sum, 2), 'day_st': day_st,
            'swap_sum': round(swap_sum, 2), 'url_statement': url_statement,
            }
    return context


@login_required
def index(request):
    df = df_db()
    deposit = deposit_sum()
    withdrawal = withdrawal_sum()
    wallet_all = wallet()
    days = days_count()
    trade_count = transactions()
    # --- data to chart ---
    df['close_time'] = pd.to_datetime(df['close_time']).dt.date
    url_statements = list(set(df['close_time']))
    url_statements.sort()
    labels, chartdata = [], []
    day_profit, label_id = 0, 0
    for url_stat in url_statements:
        day_st = df.loc[df['close_time'] == url_stat]
        commission_day = day_st.commission.sum()
        swap_day = day_st.swap.sum()
        sum_profit = 0
        for i in day_st.profit:
            if i > 0:
                sum_profit += i
        loss_profit = 0
        for i in day_st.profit:
            if i < 0:
                loss_profit += i
        day_sum = sum_profit + commission_day + loss_profit
        day_profit += day_sum + swap_day
        label_id += 1
        labels.append(label_id)
        chartdata.append(deposit + day_profit)
    # -------------------------
    context = {'deposit': deposit, 'withdrawal': withdrawal,
               'wallet_all': wallet_all, 'days': days, 'labels': labels,
               'chartdata': chartdata, 'trade_count': trade_count}
    return render(request, 'cfd/index.html', context)


@login_required
def deposit(request):
    depo = depo_db()
    sum = deposit_sum()
    context = {'depo': depo, 'sum': sum}
    return render(request, 'cfd/deposit.html', context)


@login_required
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


@login_required
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


@login_required
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


@login_required
def withdrawal(request):
    wdd = wd_db()
    sum = withdrawal_sum()
    context = {'wdd': wdd, 'sum': sum}
    return render(request, 'cfd/withdrawal.html', context)


@login_required
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


@login_required
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


@login_required
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


@login_required
def statement(request):
    context = f_stat()
    return render(request, 'cfd/statementt.html', context)


@login_required
def new_statement(request):
    # --- Read data from Excel file ---
    df = pd.read_excel(request.FILES['filexls'])
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
    # --- Convert the column type from string to datetime format ---
    df['open_time'] = pd.to_datetime(df['open_time'])
    df['close_time'] = pd.to_datetime(df['close_time'])
    # --- conect to SQL database ---
    engine = create_engine('mysql+pymysql://nook17_nook17:Nook,1771@localhost:3306/nook17_statement')
    # --- Write to database ---
    df.to_sql(
            name='cfd_statement',
            con=engine,
            index=True,
            index_label='id',
            if_exists='append',
            # if_exists='replace',
            )
    return redirect('cfd:statement')


@login_required
def statements(request, url_statement):
    context = f_stats(url_statement)
    return render(request, 'cfd/statementts.html', context)


@login_required
def delete_statement(request, ticket_id, url_statement):
    stat = stat_db()
    try:
        delstat = Statement.objects.get(ticket=ticket_id)
    except Statement.DoesNotExist:
        return redirect('cfd:statements')
    delstat.delete()
    context = f_stats(url_statement)
    return render(request, 'cfd/statementts.html', context)


@login_required
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


@login_required
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


@login_required
def calc(request):
    cal = Notesdb.objects.all().values()
    buy_level = Buy_calc.objects.all().values().order_by('-buy_level')
    df_cal = pd.DataFrame(cal)
    df_buy = pd.DataFrame(buy_level)
    wall = wallet()
    try:
        df_buy.sort_values('buy_level', ascending=False, inplace=True)
        buy_levels = df_buy.values.tolist()
    except KeyError:
        buy_levels = [1]
    if not len(df_cal.columns) == 0:
        filt = (df_cal['id'] == 2)
        gap = int(df_cal.loc[filt, 'gap'])
        lot = float(df_cal.loc[filt, 'lot'])
        margin_value = int(df_cal.loc[filt, 'margin_value'])
        pip_value = float(df_cal.loc[filt, 'pip_value'])
        tp = int(df_cal.loc[filt, 'tp'])
        select = df_cal.at[1, 'buy_or_sell']
    else:
        variables = 'default'   # temporary values
    profit_levels = []
    percent_by_wallet = ((df_buy.shape[0] * lot * margin_value * 100)/wall*100)
    for lev in Buy_calc.objects.values_list('buy_level', flat=True).order_by('-buy_level'):
        if select == 'Long':
            profit_levels.append((tp-lev)*(pip_value*lot*100))
        elif select == 'Short':
            profit_levels.append((lev-tp)*(pip_value*lot*100))

    buy_zip = list(zip(profit_levels, buy_levels))
    sum_profit = sum(profit_levels)
    context = {'gap': gap, 'lot': lot, 'margin_value': margin_value,
               'pip_value': pip_value, 'tp': tp, 'select': select,
               'sum_profit': sum_profit, 'buy_zip': buy_zip,
               'percent_by_wallet': percent_by_wallet}
    return render(request, 'cfd/calc.html', context)


@login_required
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


@login_required
def calc_buy_create(request):
    if request.method != 'POST':
        form = Buy_calcForm()
    else:
        form = Buy_calcForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('cfd:calc')
    return render(request, 'cfd/calc.html')


@login_required
def calc_buy_delete(request, buy_id):
    try:
        cbd = Buy_calc.objects.get(id=buy_id)
    except Buy_calc.DoesNotExist:
        return redirect('cfd:calc')
    cbd.delete()
    return HttpResponseRedirect(reverse('cfd:calc'))


@login_required
def pipmargin(request):
    df = pipmargin_db_pandas()
    last_margin = df.resample('D', on='updated_at')['margin'].max()
    last_pip = df.resample('D', on='updated_at')['pip'].max()
    lvol = []
    lmargin1, lpip1, lmargin2, lpip2, lmargin3, lpip3, = [], [], [], [], [], []
    lmargin4, lpip4, lmargin5, lpip5, lmargin6, lpip6, = [], [], [], [], [], []
    for i in range(6):
        i += 1
        filt = df['id'] == i
        margin = int(df.loc[filt, 'margin'])
        pip = float(df.loc[filt, 'pip'])
        for l in range(100):
            locals()['lpip%s' % i].append(pip*(l+1))
            locals()['lmargin%s' % i].append(margin*(l+1))
    for i in range(100):
        i += 1
        lvol.append(i/100)
    lists = list(zip(lmargin1, lpip1, lmargin2, lpip2, lmargin3, lpip3,
                     lmargin4, lpip4, lmargin5, lpip5, lmargin6, lpip6))
    dicts = dict(zip(lvol, lists))
    context = {'last_pip': float(last_pip), 'last_margin': int(last_margin),
               'dicts': dicts}    
    return render(request, 'cfd/pipmargin.html', context)


@login_required
def pipmargin_set(request):
    try:
        marketdb = Pipmargin.objects.get(market=request.POST.get('market'))
        if request.method != 'POST':
            form = PipmarginForm(instance=marketdb)
        else:
            form = PipmarginForm(instance=marketdb, data=request.POST)
            if form.is_valid():
                form.save()
                return redirect('cfd:pipmargin')
    except Exception:
        form = PipmarginForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('cfd:pipmargin')
    return render(request, 'cfd/pipmargin.html')


@login_required
def daily(request):
    today_is = time.strftime("%A - %d %B %Y")
    wall = wallet()
    divide_by = [0.5, 0.33, 0.25, 0.20, 0.1, 0.05, 0.02]
    percent_by = [0.5, 0.7, 1, 1.5, 2, 2.5, 3]
    threshold, margin, percent, profit = [], [], [], []
    for m in divide_by:
        threshold.append(m*100)
        margin.append(m*wall)
    for p in percent_by:
        percent.append(p)
        profit.append(p*wall/100)
    margin_by = list(zip(threshold, margin))
    profit_by = list(zip(percent, profit))
    context = {'today_is': today_is, 'wall': wall, 'margin_by': margin_by,
               'profit_by': profit_by}
    return render(request, 'cfd/daily.html', context)


@login_required
def point(request):
    df = pipmargin_db_pandas()
    per = Notesdb.objects.all().values()
    df_notes = pd.DataFrame(per)
    pip_val_markets = df['pip'].tolist()
    filt = (df_notes['id'] == 4)
    daily_p = int(df_notes.loc[filt, 'daily_point'])
    lot_v = float(df_notes.loc[filt, 'lot_value'])
    l_description = ['day', 'week', 'month', 'quarter', 'year']
    l_multiplier = [1, 5, 22, 64, 253]
    l_points, l_profit = [], []
    lpoint1, lpoint2, lpoint3, lpoint4, lpoint5, lpoint6=[],[],[],[],[],[] 
    lprofit1, lprofit2, lprofit3, lprofit4, lprofit5, lprofit6=[],[],[],[],[],[] 
    for p in range(1, 7):
        for i in l_multiplier:
            locals()['lpoint%s' % p].append(daily_p*i)
            locals()['lprofit%s' % p].append(lot_v*pip_val_markets[p-1]*daily_p*i*100)
            # l_points.append(daily_p*i)
            # l_profit.append(lot_v * daily_p*i)
    lists = list(zip(l_description, l_multiplier, lpoint1, lprofit1,
                     lpoint2, lprofit2, lpoint3, lprofit3, lpoint4,
                     lprofit4, lpoint5, lprofit5, lpoint6, lprofit6))
    context = {'lists': lists, 'daily_p': daily_p,
            'lot_v': lot_v, 'pip_val_markets': pip_val_markets}
    return render(request, 'cfd/point.html', context)


@login_required
def point_set(request):
    try:
        notes = Notesdb.objects.get(id=4)
        if request.method != 'POST':
            form = NotesdbForm(instance=notes)
        else:
            form = NotesdbForm(instance=notes, data=request.POST)
            if form.is_valid():
                form.save()
                return redirect('cfd:point')
    except Exception:
        form = NotesdbForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('cfd:point')
    return render(request, 'cfd/point.html')


@login_required
def quarter(request):
    depo_sum = depo_db_pandas()
    if not depo_sum.empty:
        deposit_sum = depo_sum.amount_dep.sum()
    else:
        deposit_sum = 0
    per = Notesdb.objects.all().values()
    qrt = Quarter.objects.all().values()
    df_notes = pd.DataFrame(per)
    df_qrt = pd.DataFrame(qrt)
    qrt_row_number = df_qrt.shape[0]
    if not len(df_notes.columns) == 0:
        filt = (df_notes['id'] == 3)
        percent_1 = float(df_notes.loc[filt, 'percent_1'])
        percent_2 = float(df_notes.loc[filt, 'percent_2'])
        percent_3 = float(df_notes.loc[filt, 'percent_3'])
        amount_base = int(df_notes.loc[filt, 'amount_quarter'])
        perc = [percent_1, percent_2, percent_3]
    else:
        percent_1 = 1
        amount_base = 1000
    lsum_1, lsum_2, lsum_3 = [], [], []
    flag = 0
    for per in perc:
        amount = amount_base
        l1, l2, l3, lper, lsum = [], [], [], [], []
        ldate, lprof, lperc, ldayprof = [], [], [], []
        flag += 1
        for i in range(66):
            l1.append(amount)
            numb = (amount * per) / 100
            amount += numb
            l2.append(numb)
            l3.append(amount)
            lper.append(((amount - amount_base) / amount_base) * 100)
            if qrt_row_number > i:
                lprof.append(int(df_qrt.loc[df_qrt['id'] == i+1, 'profit']))
                if i == 0:
                    lperc.append(((lprof[i] - amount_base) / amount_base) * 100)
                    ldayprof.append(lprof[i] - amount_base)
                else:
                    lperc.append(((lprof[i] - lprof[i-1]) / lprof[i-1]) * 100)
                    ldayprof.append(lprof[i] - lprof[i-1])
            else:
                lprof.append(0)
                lperc.append(0)
                ldayprof.append(0)

        # --- Make Date list ---
        df_qrt['date'] = pd.to_datetime(df_qrt['date']).dt.date
        dtd = df_qrt['date'].tolist()
        for url_stat in dtd:
            ldate.append(url_stat.strftime('%d-%b'))
        for i in range(66):
            if i >= len(ldate):
                ldate.append(0)
        # --- Last value in batabase ---
        last_id = df_qrt['id'].iloc[-1]
        last_dt = df_qrt['date'].iloc[-1].strftime('%Y-%m-%d')
        last_pr = df_qrt['profit'].iloc[-1]
        # --- AVG, MAX - perc & prof ---
        avg_perc = sum(lperc) / qrt_row_number
        avg_prof = sum(ldayprof) / qrt_row_number 
        max_perc = ((last_pr - amount_base) / amount_base) * 100 
        max_prof = sum(ldayprof)
        wallet = max_prof + deposit_sum
        # --- zip list ---
        if flag == 1:
            # --- Sum Q1 profit per month ---
            for i in range(1, 4):
                lsum_1.append(l3[(i*22)-1] - l1[(i*22)-22])
            lists_1 = list(zip(l1, l2, l3, lper, ldate, lprof, lperc, ldayprof))
        elif flag == 2:
            # --- Sum Q2 profit per month ---
            for i in range(1, 4):
                lsum_2.append(l3[(i*22)-1] - l1[(i*22)-22])
            lists_2 = list(zip(l1, l2, l3, lper, ldate, lprof, lperc, ldayprof))
        elif flag == 3:
            # --- Sum Q3 profit per month ---
            for i in range(1, 4):
                lsum_3.append(l3[(i*22)-1] - l1[(i*22)-22])
            lists_3 = list(zip(l1, l2, l3, lper, ldate, lprof, lperc, ldayprof))
    lsum = list(zip(lsum_1, lsum_2, lsum_3))
    context = {'percent_1': percent_1, 'percent_2': percent_2,
               'percent_3': percent_3, 'amount_base': amount_base,
               'lists_1': lists_1, 'lists_2': lists_2, 'lists_3': lists_3,
               'lsum': lsum, 'last_id': last_id, 'last_dt': last_dt,
               'last_pr': last_pr, 'avg_perc': avg_perc, 'avg_prof': avg_prof,
               'max_perc': max_perc, 'max_prof': max_prof, 'wallet': wallet}
    return render(request, 'cfd/quarter.html', context)
# ALTER TABLE `cfd_quarter` AUTO_INCREMENT=5


@login_required
def quarter_set(request):
    try:
        qrt = Quarter.objects.get(id=request.POST.get('id'))
        if request.method != 'POST':
            form = QuarterForm(instance=qrt)
        else:
            form = QuarterForm(instance=qrt, data=request.POST)
            if form.is_valid():
                form.save()
                return redirect('cfd:quarter')
    except Exception:
        form = QuarterForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('cfd:quarter')
    return render(request, 'cfd/quarter.html')


@login_required
def quarter_set_percent(request):
    try:
        notes = Notesdb.objects.get(id=3)
        if request.method != 'POST':
            form = NotesdbForm(instance=notes)
        else:
            form = NotesdbForm(instance=notes, data=request.POST)
            if form.is_valid():
                form.save()
                return redirect('cfd:quarter')
    except Exception:
        form = NotesdbForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('cfd:quarter')
    return render(request, 'cfd/quarter.html')


class ChartData(APIView):
    def get(self, request, format = None):
        df = df_db()
        df['close_time'] = pd.to_datetime(df['close_time']).dt.date
        url_statements = list(set(df['close_time']))
        url_statements.sort()
        labels, chartdata = [], []
        for url_stat in url_statements:
            day_st = df.loc[df['close_time'] == url_stat]
            commission_day = day_st.commission.sum()
            swap_day = day_st.swap.sum()
            sum_profit = 0
            for i in day_st.profit:
                if i > 0:
                    sum_profit += i
            loss_profit = 0
            for i in day_st.profit:
                if i < 0:
                    loss_profit += i
            day_sum = sum_profit + commission_day + loss_profit
            labels.append(url_stat.strftime('%d-%m'))
            chartdata.append(int(day_sum) + int(swap_day))

        chartLabel = "Daily transactions"
        data ={
                    "labels":labels,
                    "chartLabel":chartLabel,
                    "chartdata":chartdata,
            }
        return Response(data)
