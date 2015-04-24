from django.conf.urls import patterns, include, url

from django.contrib import admin
from views.index import *
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', index),


    # url(r'^blog/', include('blog.urls')),
    url(r'^getback/', getback),
    url(r'^setvalue/', setvalue),
    url(r'^getvalue/', getvalue),
    url(r'^delvalue/', delvalue),
    url(r'^listvalue/', listvalue),
    url(r'^mapvalue/', mapvalue),
    url(r'^admin/', include(admin.site.urls)),
)
