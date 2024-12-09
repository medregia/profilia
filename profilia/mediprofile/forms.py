from django import forms
from mediprofile.models import Section1

class ProfileForm(forms.ModelForm):
    
    class Meta:
        model = Section1
        fields = '__all__'
