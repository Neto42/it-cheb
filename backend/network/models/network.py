from django.db import models

from statement.models import Statement


class Network(models.Model):
    statement = models.OneToOneField(
        Statement,
        on_delete=models.CASCADE
    )
    passability = models.IntegerField()
    place = models.CharField(max_length=25)
    object_type = models.CharField(max_length=30)


class Rezult(models.Model):
    Network = models.OneToOneField(
        Network,
        on_delete=models.CASCADE
    )
    rezult = models.BooleanField()

