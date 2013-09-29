from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib import admin
from . import views

admin.autodiscover()

urlpatterns = patterns('',
    url(r"^$", views.HomepageView.as_view(), name="home"),
    url(r"^pangaea/", include("topics.urls", namespace="topics")),
    url(r"^admin/", include(admin.site.urls)),
    url(r"^accounts/", include('registration.backends.default.urls')),
)

urlpatterns += patterns('',
    (r'^static/(.*)$', 'django.views.static.serve', {
        'document_root': settings.STATIC_ROOT
    }),
    (r'^media/(.*)$','django.views.static.serve', {
        'document_root': settings.MEDIA_ROOT
    }),
)
