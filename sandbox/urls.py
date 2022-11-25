import django
from django.conf import settings
from django.conf.urls import include
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.sitemaps import views
from oscar.app import application
from oscar.views import handler403, handler404, handler500

from apps.gateway import urls as gateway_urls
from apps.sitemaps import base_sitemaps
from django.urls import path, re_path

admin.autodiscover()

urlpatterns = [
    # Include admin as convenience. It's unsupported and only included
    # for developers.
    path('admin/', include(admin.site.urls)),

    # i18n URLS need to live outside of i18n_patterns scope of Oscar
    path('i18n/', include(django.conf.urls.i18n)),

    # include a basic sitemap
    re_path(r'^sitemap\.xml$', views.index,
        {'sitemaps': base_sitemaps}),
    re_path(r'^sitemap-(?P<section>.+)\.xml$', views.sitemap,
        {'sitemaps': base_sitemaps},
        name='django.contrib.sitemaps.views.sitemap')
]

# Prefix Oscar URLs with language codes
urlpatterns += i18n_patterns(
    # Custom functionality to allow dashboard users to be created
    path('gateway/', include(gateway_urls)),
    # Oscar's normal URLs
    path('', application.urls),
)

if settings.DEBUG:
    import debug_toolbar

    # Server statics and uploaded media
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
    # Allow error pages to be tested
    urlpatterns += [
        path('403', handler403),
        path('404', handler404),
        path('500', handler500),
        path('__debug__/', include(debug_toolbar.urls)),
    ]
