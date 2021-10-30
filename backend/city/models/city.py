from django.db import models


class City(models.Model):
    city = models.CharField(max_length=100, verbose_name='Город')
    district = models.CharField(max_length=100, verbose_name='Район')
    street = models.CharField(max_length=100, verbose_name='Улица')
    house = models.CharField(max_length=100, verbose_name='Дом')

    def __str__(self):
        return self.street