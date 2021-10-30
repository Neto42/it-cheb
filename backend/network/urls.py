from django.urls import path, include

from network.views.views import NetworkList

urlpatterns = [
    path('', NetworkList().as_view()),
]
