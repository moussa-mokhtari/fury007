from django.contrib import admin
from django.conf.urls import patterns, include, url

urlpatterns = patterns('space_manager.views',
	                 url(r'^show$', 'space_show'),
	                 url(r'^settings$', 'settings_show'),
	                 
             

                                          
    # Examples:
    # url(r'^$', 'RyadEssalihine.views.home', name='home'),
    # url(r'^RyadEssalihine/', include('RyadEssalihine.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)