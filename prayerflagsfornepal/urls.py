from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from flags import views
import os

urlpatterns = [
    # Examples:
    # url(r'^$', 'prayerflagsfornepal.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.index, name='index'),
    url(r'^flags/([0-9]+)', views.single, name='singleFlag'),
    url(r'^get', views.getFlags, name='getFlags'),
    url(r'^flag', views.flagFlag, name='flagFlags'),
    url(r'^terms', views.terms, name='terms'),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
    {'document_root': settings.MEDIA_ROOT}),
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve',
    {'document_root': settings.STATIC_ROOT}),
]
