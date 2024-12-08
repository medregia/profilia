from django.contrib import admin
from mediprofile.models import Section1

# @admin.register(profile)
class ProfileAdmin(admin.ModelAdmin):
    list=['category_name',  'dlnumber_1','dlnumber_2', 'dlnumber_3', 'dlnumber_4', 'dlnumber_5', 'dlnumber_6', 'dlnumber_7', 'dlnumber_8', 'dlnumber_9']
    
admin.site.register(Section1,ProfileAdmin)


# Register your models here.
