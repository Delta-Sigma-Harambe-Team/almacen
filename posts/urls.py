from django.conf.urls import url, include
from rest_framework_nested import routers
from posts.views import PostViewSet,AccountPostsViewSet

router = routers.SimpleRouter()
router.register(r'posts', PostViewSet)

accounts_router = routers.NestedSimpleRouter(router, r'posts', lookup='account')
accounts_router.register(r'accounts', AccountPostsViewSet,base_name = 'posts-accounts')

urlpatterns = [
	url(r'^api/v1/', include(router.urls)),
  	url(r'^api/v1/', include(accounts_router.urls)),
]

