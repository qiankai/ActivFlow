"""URL configuration for django app"""

from django.conf.urls import include, url
from django.contrib import admin


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^auth/', include('django.contrib.auth.urls')),
    url(r'', include('activflow.core.urls')),
    url(r'^employee/',include('employee.urls'))
]
