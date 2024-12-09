from django.shortcuts import render,redirect
from django.http import HttpResponse
from mediprofile.models import Section1
from mediprofile.forms import ProfileForm

def display(request):
    profile = Section1.objects.all()
    return render(request, 'index.html', {'profile' : profile})

def addprofile(request):
    form = ProfileForm()
    if request.method == 'POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/kk')
    return render(request, 'create.html', {'form' : form})

def deleteview(request, id):
    form = Section1.objects.get(id=id)
    form.delete()
    return redirect('/kk')
    
