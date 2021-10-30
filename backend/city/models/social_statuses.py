from django.db import models


class SocialStatuses(models.Model):
    social_statuses = models.CharField(max_length=50)

    def __str__(self):
        return self.social_statuses