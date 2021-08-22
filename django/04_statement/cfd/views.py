from django.shortcuts import render
from .models import Statement
import pandas as pd
from datetime import datetime

# url_statements = [
#         '2021.05.31',
#         '2021.06.01',
#         '2021.06.02',
#         '2021.06.08',
#         '2021.06.09'
#         ]

def df_db():
    statements = Statement.objects.all().values()
    df = pd.DataFrame(statements)
    return df

# Create your views here.
def index(request):
    return render(request, 'cfd/index.html')

def statement(request):
    df = df_db()
    all_sum = df.profit.sum()
    # df_context = {'df': df.to_html()}
    day_statement = list(df['open_time'].apply(lambda x: x.split(' ')[0] if len(x) > 10 else x))
    url_statements = list(set(day_statement))
    url_statements.sort(key = lambda date: datetime.strptime(date, '%Y.%m.%d'))
    df_context = {'all_sum': all_sum, 'url_statements': url_statements}
    return render(request, 'cfd/statement.html', context=df_context)

def statements(request, url_statement):
    df = df_db()
    day_st = df[df['open_time'].str[:10] == url_statement]
    day_sum = day_st.profit.sum()
    short_day_sum = round(day_sum, 2)
    day_real = datetime.strptime(url_statement, '%Y.%m.%d')
    format_day = day_real.strftime('%A - %d %B %Y')
    context = {'format_day': format_day, 'day_st': day_st.to_html(), 'short_day_sum': short_day_sum}
    return render(request, 'cfd/statements.html', context)
