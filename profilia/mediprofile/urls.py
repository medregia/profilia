from django.contrib import admin
from django.urls import path
from mediprofile import views

urlpatterns = [
    path('kk', views.display, name="index" ),
]
