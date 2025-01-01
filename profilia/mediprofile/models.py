from django.db import models

class Section1(models.Model):
    category_name = models.CharField(max_length=51)
    dl1 = models.CharField(max_length=13, unique=True) 
    dl2 = models.CharField(max_length=13, unique=True) 

    def __str__(self):
        return f"{self.category_name} ({self.dl1}, {self.dl2})"

class AdditionalDLNumber(models.Model):
    section = models.ForeignKey(Section1, on_delete=models.CASCADE, related_name="additional_dl_numbers")
    dl_number = models.CharField(max_length=13, unique=True)  # Optional but unique across the system

    def __str__(self):
        return f"{self.section.category_name} - {self.dl_number}"
