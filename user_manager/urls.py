from django.contrib import admin
from django.conf.urls import patterns, include, url

urlpatterns = patterns('user_manager.views',
	                 url(r'^sign-in$', 'signin'),
                     url(r'^sign-up$','signup'),
	                 url(r'^sign-out$', 'signout'),
                     url(r'^subscribe$', 'subscribe'),
                     url(r'^users$', 'user_list'),
                     url(r'^user$', 'user_get'),
	                 

                                         
    # Examples:
    # url(r'^$', 'RyadEssalihine.views.home', name='home'),
    # url(r'^RyadEssalihine/', include('RyadEssalihine.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
