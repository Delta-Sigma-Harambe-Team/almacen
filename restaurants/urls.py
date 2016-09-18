from django.conf.urls import url, include
from rest_framework_nested import routers
from .views import OrderViewSet

router = routers.SimpleRouter()
router.register(r'orders', OrderViewSet)

urlpatterns = [
	url(r'^api/v1/', include(router.urls)),
]