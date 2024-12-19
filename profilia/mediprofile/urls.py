from django.contrib import admin
from django.urls import path
from mediprofile import views

urlpatterns = [
    path('kk/', views.display, name="index"),
    path('ss/', views.addprofile, name="addprofile"),
    path('delete/<int:id>/', views.deleteview, name="deleteview"),
    path('edit/<int:id>/', views.editview, name="editview"),
]

