from django.urls import path
from . import views

app_name = 'cfd'
urlpatterns = [
    path('', views.index, name='index'),
    path('statement/', views.statement, name='statement'),
    path('statement/<str:url_statement>/', views.statements, name='statements'),
    path('api', views.ChartData.as_view()),
    path('deposit/', views.deposit, name='deposit'),
    path('new_deposit/', views.new_deposit, name='new_deposit'),
    path('update_deposit/<int:deposit_id>/', views.update_deposit, name='update_deposit'),
    path('delete_deposit/<int:deposit_id>/', views.delete_deposit, name='delete_deposit'),
    path('withdrawal/', views.withdrawal, name='withdrawal'),
    path('new_withdrawal/', views.new_withdrawal, name='new_withdrawal'),
    path('update_withdrawal/<int:withdrawal_id>/', views.update_withdrawal, name='update_withdrawal'),
    path('delete_withdrawal/<int:withdrawal_id>/', views.delete_withdrawal, name='delete_withdrawal'),
    path('year/', views.year, name='year'),
    path('year/set', views.new_percent, name='new_percent'),
    path('calc/', views.calc, name='calc'),
    path('calc/set', views.calc_set, name='calc_set'),
    path('calc/buy_create', views.calc_buy_create, name='calc_buy_create'),
    # path('calc/buy_update/<int:buy_id>/', views.calc_buy_update, name='calc_buy_update'),
    path('calc/buy_delete/<int:buy_id>/', views.calc_buy_delete, name='calc_buy_delete'),
    ]
