from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
                 # Examples:
                 #url that shows the home page .HADJI HICHAM 
                 url(r'^$', 'whatsappme.views.Home', name='home'),
                 #url that shows usermanager app 
                 url(r'^user/', include('user_manager.urls')),
                 url(r'^(?P<username>[0-9a-zA-Z_-]+)/$','user_manager.views.user_space'),
              

                 # url that shows user space (space_manager app)
                 url(r'^space/', include('space_manager.urls')),
                 #url that shows the rest APIS
                 url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
                 # url(r'^blog/', include('blog.urls')),
                 #url for admin app
                 url(r'^admin/', include(admin.site.urls)),
]
