from django.conf.urls import patterns, url, include
from almacen.views import IndexView
from rest_framework_nested import routers
from authentication.views import *
from django.contrib import admin

urlpatterns = patterns(
     '',
    url(r'^admin/', admin.site.urls),
    url(r'^', include('authentication.urls', namespace='auth')),   
    url('^.*$', IndexView.as_view(), name='index'),
)