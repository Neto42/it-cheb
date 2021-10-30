from django.urls import path, include

from city.views.views import SocialStatusesList, CityList, PopulationList

urlpatterns = [
    path('', CityList().as_view()),
    path('social/', SocialStatusesList().as_view()),
    path('population/', PopulationList().as_view()),
]
