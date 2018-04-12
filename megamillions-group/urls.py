from django.urls import include, path, re_path
from django.contrib import admin
from results.views import results, matchingTickets
from django.conf import settings

urlpatterns = [
    re_path(r'^', include('results.urls')),
    re_path(r'^results/', include('results.urls')),
    path('admin/', admin.site.urls),
    re_path(r'^results/(\d+)/(\d+)/$', matchingTickets),
    re_path(r'^results/(\d+)/$', results),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        re_path(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns