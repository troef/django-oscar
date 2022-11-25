from django.conf.urls import include
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from oscar.app import application
from django.urls import path

admin.autodiscover()

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', application.urls),
    path('i18n/', include('django.conf.urls.i18n')),
]
urlpatterns += staticfiles_urlpatterns()
