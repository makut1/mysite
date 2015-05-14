from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
   # url(r'^$', 'mysite.views.home', name='home'),
     #url(r'^blog/', include('blog.urls')),
#url(r'', include('blog.urls')),
     url(r'^admin/', include(admin.site.urls)),
	 url(r'^$', 'article.views.home'),
	 #url(r'^(?P<my_args>\d+)/$', 'article.views.detail', name='detail'),
	 url(r'^test/$', 'article.views.test',name='test'),
	 url(r'^(?P<id>\d+)/$', 'article.views.detail', name='detail'),
	#url(r'^hello/', include(hello.urls)),
)
