from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='members'),
    path('', views.execute_prompt_vue, name='execute_prompt_vue')
    ]
