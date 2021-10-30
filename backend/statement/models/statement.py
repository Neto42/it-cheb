from django.db import models
from django.utils import timezone

from city.models import City, SocialStatuses

MALE = 'Мужской'
FEMALE = 'Женский'
GENDER = (
    (MALE, 'Мужской'),
    (FEMALE, 'Женский')
)


class Statement(models.Model):
    email_user = models.EmailField(max_length=50)

    city = models.ForeignKey(
        City,
        on_delete=models.SET_NULL,
        null=True, blank=True
    )
    gender = models.CharField(max_length=10, choices=GENDER, default=MALE)
    age = models.IntegerField()
    social = models.ForeignKey(
        SocialStatuses,
        on_delete=models.SET_NULL,
        null=True, blank=True
    )

    complaint = models.TextField()
    date = models.DateTimeField(default=timezone.now())


