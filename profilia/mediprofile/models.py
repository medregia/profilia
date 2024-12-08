from django.db import models

class Section1(models.Model):
    category_name = models.CharField(max_length=51)
    dlnumber_1 = models.CharField(max_length=13, primary_key=True)
    dlnumber_2 = models.CharField(max_length=13)
    dlnumber_3 = models.CharField(max_length=13)
    dlnumber_4 = models.CharField(max_length=13)
    dlnumber_5 = models.CharField(max_length=13)
    dlnumber_6 = models.CharField(max_length=13)
    dlnumber_7 = models.CharField(max_length=13)
    dlnumber_8 = models.CharField(max_length=13)
    dlnumber_9 = models.CharField(max_length=13)


    def __str__(self):
        return self.category_name
