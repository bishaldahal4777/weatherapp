from django.urls import path
from django import views

urlpatterns = [
    path('', views.index, name="home"),
]
