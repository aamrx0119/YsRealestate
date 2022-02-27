from django.db import models

# Create your models here.


class House_model (models.Model):
    name = models.CharField(max_length=50)
    information = models.TextField(max_length=500)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
