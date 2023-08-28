from django.db import models

# Create your models here.
class unislot(models.Model):
    name=models.CharField(max_length=200)
    desc=models.CharField(max_length=200)
    image=models.ImageField(upload_to='image')
    location=models.CharField(max_length=200)

    def __str__(self):
        return self.name
