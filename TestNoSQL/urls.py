from django.conf.urls import patterns, include, url

from django.contrib import admin
from views.index import *
from views.testMemcached import *
from views.testMongo import *

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
    url(r'^testinsert/', testInsert),
    url(r'^testdel/', testDelete),
    url(r'^testfind/', testfind),
    url(r'^testmaprduce/', testMapduce),
    url(r'^testupdate/', testUpdate),
    url(r'^testremove/', testRemove),
    url(r'^mtestset/', mtestSet),
    url(r'^mtestget/', mtestGet),
    url(r'^mtestadd/', mtestAdd),
    url(r'^mtestappend/', mtestAppend),
    url(r'^mtestdelete/', mtestDelete),
    url(r'^mtestgetMulti/', mtestGetMulti),
    url(r'^mtestincr/', mtestIncr),
    url(r'^mtestdecr/', mtestDecr),
    url(r'^mtestreplace/', mtestReplace),
    url(r'^mteststats/', mtestStats),
    url(r'^admin/', include(admin.site.urls)),
)
