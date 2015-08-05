from django.conf.urls import include, url
from django.contrib import admin

from football import urls as football_urls

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^football-api/', include(football)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))

]
