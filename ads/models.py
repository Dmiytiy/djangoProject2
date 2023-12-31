from django.db import models

# Create your models here.
class Ad(models.Model):
    name = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    price = models.PositiveIntegerField()
    description = models.TextField(null=True)
    address = models.CharField(max_length=100)
    is_poblished = models.BooleanField()

class Category(models.Model):
    name = models.CharField(max_length=100)