from django.db import models

class Animal(models.Model):
    name = models.CharField(max_length=50)
    age = models.FloatField(min_value=0)
    weight = models.FloatField(min_value=0)
    sex = models.CharField(max_length=15)