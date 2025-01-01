from django.contrib import admin
from django.urls import path
from mediprofile import views

urlpatterns = [
    path('index/', views.display, name="index"),
    path('add/', views.addprofile, name="addprofile"),
    path('delete/<int:id>/', views.deleteview, name="deleteview"),
    path('edit/<int:id>/', views.edit_profile, name="edit_profile"),
]

