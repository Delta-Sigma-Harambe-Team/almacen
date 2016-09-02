from django.conf.urls import url, include
from rest_framework_nested import routers
from posts.views import PostViewSet,AccountPostsViewSet

router = routers.SimpleRouter()
router.register(r'posts', PostViewSet)

#Imports de Authentications
from authentication.views import AccountViewSet
router.register(r'accounts', AccountViewSet) 

accounts_router = routers.NestedSimpleRouter(router, r'accounts', lookup='account')
accounts_router.register(r'posts', AccountPostsViewSet,base_name = 'posts-accounts')

urlpatterns = [
	url(r'^api/v1/', include(router.urls)),
  	url(r'^api/v1/', include(accounts_router.urls)),
]