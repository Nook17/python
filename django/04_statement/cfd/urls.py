from django.urls import path
from . import views

app_name = 'cfd'
urlpatterns = [
    path('', views.index, name='index'),
    path('statement/', views.statement, name='statement'),
    path('statement/<str:url_statement>/', views.statements, name='statements'),
    ]
