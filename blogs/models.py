from django.db import models
from django.db.models.base import Model

STATUS = (
    (0, "Draft"),
    (1, "Publish")
)
# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=20)
    image = models.ImageField(upload_to='images/')
    description = models.CharField(max_length=200)
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ['-created_on']    

    def __str__(self):
        return self.title 