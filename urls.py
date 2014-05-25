from django.conf.urls import patterns, include, url

from django.contrib import admin

import auth.views
import users.views
import MyGodness.views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'HerokuTest.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    #url(r'^admin/', include(admin.site.urls)),
    url(r'^$', MyGodness.views.IndexView.as_view(), name = 'index'),
    url(r'personal-info', users.views.PersonInfoView.as_view(), name = 'personinfo'),
    url(r'^login$', auth.views.LoginView.as_view(), name = 'login'),
    url(r'^register$', auth.views.RegisterView.as_view(), name = 'register'),
)

urlpatterns += patterns('django.contrib.staticfiles.views',
        url(r'^static/(?P<path>.*)$', 'serve'),
    )
