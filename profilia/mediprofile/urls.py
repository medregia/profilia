from django.contrib import admin
from django.urls import path
from mediprofile import views

urlpatterns = [
    path('kk/', views.display, name="index" ),
    path('ss/', views.addprofile, name="addprofile"),
    path('delete/<id>', views.deleteview, name="deleteview" ),
]
