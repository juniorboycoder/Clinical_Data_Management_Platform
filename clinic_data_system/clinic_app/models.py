from django.db import models

# Create your models here.
from django.db import models

# Create your models here.

class Patient(models.Model):
    name= models.CharField(max_length=200)
    Symptom1= models.CharField(max_length=100)
    Symptom2= models.CharField(max_length=100)
    def __str__(self):
	    return self.name