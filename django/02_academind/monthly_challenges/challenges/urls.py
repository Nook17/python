from django.urls import path
from . import views

app_name = 'challenges'
urlpatterns = [
        path('', views.index, name='index'),
        # path('january/', views.january, name='january'),
        # path('february/', views.february, name='february'),
        path('<nook>', views.nook_func),
        ]
