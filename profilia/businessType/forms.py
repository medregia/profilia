from django import forms
from .models import BusinessData

class ProprietorshipForm(forms.ModelForm):
    class Meta:
        model = BusinessData
        fields = [
            'business_type',
            'proprietor_name',
            'business_name',
            'pan',
            'gstin',
            'contact_number',
            'email',
        ]
        widgets = {
            'business_type' : forms.HiddenInput(attrs={'value' : 'Proprietorship'}),
        }
