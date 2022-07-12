from django.db import models

# Create your models here.
class Cart(models.Model):
    username = models.TextField()
    products = models.TextField()