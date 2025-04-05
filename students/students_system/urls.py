from django.urls import path 
from django.contrib.auth import views   as auth_views 

from .views import register, dashboard, logout
from django.contrib.auth.views import LogoutView
from django.urls import path
from .views import assignments, wellness
from django.urls import path
from . import views
from .views import register, dashboard, logout
urlpatterns = [
    path('register/', views.register, name='register') ,
    path('success_message/', views.success_message, name='success_message'),
    path('login/', views.login, name='login'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('logout/', views.logout, name='logout'),
    path('assignments/', assignments, name='assignments'),
    path('wellness/', wellness, name='wellness'),
]






