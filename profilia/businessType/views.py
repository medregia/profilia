from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseBadRequest
from django.views import View
from .forms import ProprietorshipForm

class BusinessTypeSelectionView(View):
    template_name = 'businessType/businesstype.html'
    template_name2 = 'businessType/proprietorship_form.html'    

    def get(self, request, *args, **kwargs):
        print(f"Template being rendered: {self.template_name}")
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        business_type = request.POST.get('business_type')
        if business_type:
            request.session['business_type'] = business_type
            if business_type == "Proprietorship":
                if request.method == "POST":
                    form = ProprietorshipForm(request.POST)
                    if form.is_valid():
                        form.save()
                        return redirect('/hi')
                    else:
                        return render(request, self.template_name2, {'form': form})
                else:
                    form = ProprietorshipForm()
                    return render(request, self.template_name2,{'form': form})
            else:
                return HttpResponse(" Sorry now Proprietorship only delvelop after it will update")
        else:
            return render(request, self.template_name, {'error': 'Please select a business type.'})



# ---------------------------Debugging------------------------------------
# print(f"Selected Business Type: {business_type}")  