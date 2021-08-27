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
    path('withdrawal/', views.withdrawal, name='withdrawal'),
    ]
