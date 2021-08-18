"""
Defines URL patterns for learning_logs application
learning_logs/urls.py
"""
from django.urls import path
from . import views

app_name = 'learning_logs'
urlpatterns = [
    path('', views.index, name='index'),
    path('topics/', views.topics, name='topics'),
    path('topics/<int:topic_id>/', views.topic, name='topic'),
    path('new_topic/', views.new_topic, name='new_topic'),
    path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'),
    path('update_entry/<int:entry_id>/', views.update_entry, name='update_entry'),
    path('delete_entry/<int:entry_id>/', views.delete_entry, name='delete_entry'),
    ]
