from django.urls import path
from . import views

app_name = 'challenges'
urlpatterns = [
        path('', views.index),
        path('january/', views.january),
        ]
