import json
from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse, HttpResponse
from mediprofile.models import Section1
from mediprofile.forms import ProfileForm

def display(request):
    profiles = Section1.objects.all()
    return render(request, 'index.html', {'profile': profiles})

def addprofile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/index')
    else:
        form = ProfileForm()
    return render(request, 'create.html', {'form': form})

def deleteview(request, id):
    Section1.objects.filter(id=id).delete()
    return redirect('/index')
    
def edit_profile(request, id):
    if request.method == 'POST':
        try:
            profile = Section1.objects.get(id=id)
            data = json.loads(request.body)

            fields = [ "category_name", "dl1", "dl2" ]
            for index, field in enumerate(fields, start=1):
                setattr(profile, field, data.get(f"field_{index}", getattr(profile, field)))
            profile.save()

            additional_dl_numbers = data.get("additional_dl_numbers", [])
            current_additional_dls = set(profile.additional_dl_numbers.values_list("dl_number", flat=True))

            for dl in additional_dl_numbers:
                if dl not in current_additional_dls:
                    AdditionalDLNumber.objects.create(section=profile, dl_number=dl)

            # Remove DL numbers not in the updated list
            profile.additional_dl_numbers.exclude(dl_number__in=additional_dl_numbers).delete()

            return JsonResponse({"success": True})

        except Section1.DoesNotExist:
            return JsonResponse({"success": False, "error": "Profile not found"})
    
    return JsonResponse({"success": False, "error": "Invalid Request"})
    
           
            
