from django.db import models
from django.db.models.base import Model

# Create your models here.
class Company(models.Model):
    name = models.CharField(max_length=20)
    image = models.ImageField(upload_to='images/')
    description = models.CharField(max_length=200)
    
    # makes it easier to select the company you want to pick by choosing the summary
    def __str__(self):
        return self.name  