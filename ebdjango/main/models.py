from django.db import models

# Create your models here.

class EMR(models.Model):
    nameOfPatient = models.CharField(max_length=25)
    medicalCondition = models.CharField(max_length=100)