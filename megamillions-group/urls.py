from django.conf.urls import include, url
from django.contrib import admin
from results.views import results, matchingTickets

urlpatterns = [
    url(r'^', include('results.urls')),
    url(r'^results/', include('results.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^results/(\d+)/(\d+)/$', matchingTickets),
    url(r'^results/(\d+)/$', results),
]