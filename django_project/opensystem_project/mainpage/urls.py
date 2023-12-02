from django.urls import path
from . import views

urlpatterns = [
    path('mainpage/', views.home, name='members')
    ]