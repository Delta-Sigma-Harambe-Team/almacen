from django.conf.urls import patterns, url, include
from almacen.views import IndexView
from rest_framework_nested import routers
from authentication.views import AccountViewSet ,LoginView

router = routers.SimpleRouter()
router.register(r'accounts', AccountViewSet)

urlpatterns = patterns(
     '',
    # ... URLs
    url(r'^api/v1/', include(router.urls,namespace = 'accounts')),
    url(r'^api/v1/auth/login/$', LoginView.as_view(), name='login'),
    
    url('^.*$', IndexView.as_view(), name='index'),
)