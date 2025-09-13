from django.db import models
# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=200)
    description =models.CharField(max_length=500)
    price= models.IntegerField(default=0)
    quantity = models.IntegerField(default=0)
    author = models.JSONField(default = list,blank=True)

    def __str__(self):
        return f"{self.name} by {self.author}"
