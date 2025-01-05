from django.contrib import admin
from django.urls import path
from businessType.views import BusinessTypeSelectionView

urlpatterns = [
    path('hi', BusinessTypeSelectionView.as_view(), name= 'businesstype' ),
    # path('proprietorship/', ProprietorshipView.as_view(), name='proprietorship_form'),
]

