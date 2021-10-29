from django.contrib.auth.models import AbstractUser
from django.db import models


ADMIN = 'Admin'
USER = 'User'

JOB_CHOICES = [
    (ADMIN, 'Admin'),
    (USER, 'User'),
]


class Profile(AbstractUser):
    job = models.CharField(max_length=7, choices=JOB_CHOICES, default=USER)
