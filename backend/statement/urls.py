from django.urls import path, include

from statement.views.views import StatementList

urlpatterns = [
    path('', StatementList().as_view()),
]
