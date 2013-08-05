from django.conf.urls import patterns, include, url

from api.views import *

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()


urlpatterns = patterns('api.views',
    url(r'^root/$', 'api_root'),
    url(r'^metadata', MetaDataView.as_view(), name='metadata'),
 
)