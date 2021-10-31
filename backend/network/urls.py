from django.urls import path, include

from network.views.views import NetworkList, RezultList

urlpatterns = [
    path('', NetworkList().as_view()),
    path('rezult/', RezultList().as_view()),
]
