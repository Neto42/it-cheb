from django.urls import path, include

from account.views import ProfileList

urlpatterns = [
    path('', ProfileList().as_view()),
]
