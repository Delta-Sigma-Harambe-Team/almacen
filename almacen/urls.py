from django.conf.urls import patterns, url, include
from almacen.views import IndexView
from rest_framework_nested import routers
from django.contrib import admin

urlpatterns = patterns(
     '',
    url(r'^admin/', admin.site.urls),

    url(r'^', include('authentication.urls', namespace='auth')),
    url(r'^', include('posts.urls', namespace='auth')), 

    url('^.*$', IndexView.as_view(), name='index'),
)
#url(r'^', include('posts.urls', namespace='posts')),