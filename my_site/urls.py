from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'fish_site.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', 'my_site.views.home', name = 'home'),
    url(r'^test/$', 'my_site.views.test', name = 'background_test'),
)

#These lines of code are needed for the django development server to serve media files.
from django.conf import settings

if settings.DEBUG:
    urlpatterns += patterns('',
        (r'%s(?P<path>.*)' % settings.MEDIA_URL[1:], 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    )