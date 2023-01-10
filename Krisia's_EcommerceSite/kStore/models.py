from django.db import models

# Create your models here.
class productTable(models.Model):
    prod_name = models.CharField(max_length=255)
    prod_price = models.IntegerField()
    image = models.ImageField(upload_to='images/')

class cartCounter(models.Model):
    count = models.IntegerField()