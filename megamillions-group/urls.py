from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^', include('results.urls')),
    url(r'^results/', include('results.urls')),
    url(r'^admin/', admin.site.urls),
]