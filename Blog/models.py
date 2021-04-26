from django.db import models

# Create your models here.


class myblog(models.Model):
    img = models.ImageField(max_length=100)
    name= models.CharField(max_length=50, null=True)
    about = models.TextField(null=True)
    datetime = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name