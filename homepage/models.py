from django.db import models

# Create your models here.


class books(models.Model):
    name = models.CharField(max_length=100)
    img1 = models.ImageField(upload_to='pics')
    img2 = models.ImageField(upload_to='pics')
    price = models.FloatField()
    offer = models.BooleanField(default=False)
    sold = models.BooleanField(default=False)
    author = models.CharField(max_length=100)
    condition = models.CharField(max_length=20)
