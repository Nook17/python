from django.urls import path
from . import views

app_name = 'service'
urlpatterns = [
        path('', views.index, name='index'),
        path('notify/', views.notify, name='notify'),
        path('contact', views.contact, name='contact'),
        ]
