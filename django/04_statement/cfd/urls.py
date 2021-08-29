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
    path('year', views.year, name='year'),
    path('year/new', views.new_percent, name='new_percent'),
    # path('year/newamo', views.new_amount, name='new_amount'),
    ]
