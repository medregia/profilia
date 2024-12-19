from django.shortcuts import render,redirect,  get_object_or_404
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
    
def editview(request, id):
    edit = Section1.objects.get(id=id)
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=edit)
        if form.is_valid():
            form.save()
            return redirect('/kk')
        else:
             return HttpResponse( "hi")
    return render(request, 'edit.html', {'edit':edit})