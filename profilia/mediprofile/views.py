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
            return redirect('/kk')
    else:
        form = ProfileForm()
    return render(request, 'create.html', {'form': form})



def deleteview(request, id):
    Section1.objects.filter(id=id).delete()
    return redirect('/kk')
    
def edit_profile(request, id):
    if request.method == 'POST':
        try:
            profile = Section1.objects.get(id=id)
            data = json.loads(request.body)

            fields = [
                "category_name", "dlnumber_1", "dlnumber_2", "dlnumber_3", 
                "dlnumber_4", "dlnumber_5", "dlnumber_6", "dlnumber_7", 
                "dlnumber_8", "dlnumber_9"
            ]
            for index, field in enumerate(fields, start=1):
                setattr(profile, field, data.get(f"field_{index}", getattr(profile, field)))

            profile.save()
            return JsonResponse({"success": True})
        except Section1.DoesNotExist:
            return JsonResponse({"success": False, "error": "Profile not found"})
    
    return JsonResponse({"success": False, "error": "Invalid Request"})
    
##
    #         profile.category_name = data.get("field_1", profile.category_name)
    #         profile.dlnumber_1 = data.get("field_2", profile.dlnumber_1)
    #         profile.dlnumber_2 = data.get("field_3", profile.dlnumber_2)
    #         profile.dlnumber_3 = data.get("field_4", profile.dlnumber_3)
    #         profile.dlnumber_4 = data.get("field_5", profile.dlnumber_4) 
    #         profile.dlnumber_5 = data.get("field_6", profile.dlnumber_5)
    #         profile.dlnumber_6 = data.get("field_7", profile.dlnumber_6)
    #         profile.dlnumber_7 = data.get("field_8", profile.dlnumber_7)
    #         profile.dlnumber_8 = data.get("field_9", profile.dlnumber_8)
    #         profile.dlnumber_9 = data.get("field_10", profile.dlnumber_9)
                
    #         profile.save()    
                    
    #         return JsonResponse({"success": True})
    #     except Section1.DoesNotExist:
    #         return JsonResponse({"success" : False, "error": "profile no t found"})
    
    # return JsonResponse({"sucess" : False, "error" : "Involid Request" })
           
            
