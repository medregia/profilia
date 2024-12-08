from django.shortcuts import render
from django.http import HttpResponse
from mediprofile.models import Section1

def display(request):
    profile = Section1.objects.all()
    return render(request, 'index.html', {'profile' : profile})

