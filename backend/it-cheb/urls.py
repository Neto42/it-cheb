from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('account.urls')),
    path('city/', include('city.urls')),
    path('statement/', include('statement.urls')),
    path('network/', include('network.urls'))
]
