from django.db import models
from django.db.models.base import Model

# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=15)
    image = models.ImageField(upload_to='images/')
    description = models.CharField(max_length=200)
    url = models.URLField(max_length = 200)
    
    def __str__(self):
        return self.name  