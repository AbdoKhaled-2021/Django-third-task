from django.db import models

# Create your models here.
class Student(models.Model):
    f_name = models.CharField(max_length=255) 
    l_name = models.CharField(max_length=255) 
    mobile = models.IntegerField(null=True) 
    birth_date = models.DateField(null=True)
    
    def __str__(self) -> str:
        return self.f_name + self.l_name 
    
    