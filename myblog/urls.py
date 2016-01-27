from django.conf.urls import include, url, patterns
from django.contrib import admin

from .views import index

urlpatterns = patterns('',
                       url(r'^$', index, name='index'),
                       url(r'^blogs/', include('blogs.urls')),

                       url(r'^accounts/login/$',
                           'django.contrib.auth.views.login',
                           name='auth_login'),

                       url(r'^accounts/logout/$',
                           'django.contrib.auth.views.logout',
                           name='auth_logout_next'),
                       url(r'^admin/', include(admin.site.urls)),
                       )
