from django.contrib import admin
from django.conf.urls import include, url, patterns

from .views import index

urlpatterns = patterns('',
                       url(r'^$', index, name='index'),
                       url(r'^blogs/', include('blogs.urls')),
                       url(r'^admin/', include(admin.site.urls)),
                       )
