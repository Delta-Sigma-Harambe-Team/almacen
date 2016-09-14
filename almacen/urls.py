from django.conf.urls import url, include
from almacen.views import IndexView
from rest_framework_nested import routers
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^', include('authentication.urls', namespace='auth')),
    url(r'^', include('posts.urls', namespace='posts')),
	url(r'^', include('products.urls', namespace='products')),     

    url('^.*$', IndexView.as_view(), name='index'),
]