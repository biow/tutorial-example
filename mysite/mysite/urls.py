from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^hello/$', 'trips.views.hello_world'),
    url(r'^$', 'trips.views.home'),
    url(r'^post/(?P<id>\d+)/$', 'trips.views.post_detail',
        name='post_detail'),
    url(r'^post/new/$', 'trips.views.post_new', name='post_new'),
    url(r'^post/(?P<id>\d+)/edit/$', 'trips.views.post_edit',
        name='post_edit'),
)
