from django.contrib import admin

from city.models import City, PopulationSize, SocialStatuses

admin.site.register(City)
admin.site.register(PopulationSize)
admin.site.register(SocialStatuses)
