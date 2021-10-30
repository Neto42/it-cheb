from django.db import models


class City(models.Model):
    city = models.CharField(max_length=25)
    district = models.CharField(max_length=25)
    street = models.CharField(max_length=25)
    house = models.CharField(max_length=25)

    def __str__(self):
        return self.city