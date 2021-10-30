from django.db import models

class City(models.Model):
    city = models.CharField(max_length=25)
    district = models.CharField(max_length=50)
    street = models.CharField(max_length=50)
    house = models.CharField(max_length=10)

