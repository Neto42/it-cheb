from django.db import models

from city.models import City


class PopulationSize(models.Model):
    city = models.OneToOneField(
        City,
        on_delete=models.CASCADE
    )

    population_size = models.IntegerField()
