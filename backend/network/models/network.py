from django.db import models


class Network(models.Model):
    street = models.CharField(max_length=25)
    social = models.BooleanField()
    passability = models.IntegerField()
    object_type = models.CharField(max_length=30)
    construction = models.BooleanField()


class Rezult(models.Model):
    street = models.CharField(max_length=25)
    object_type = models.CharField(max_length=25)
    rezult = models.BooleanField()


