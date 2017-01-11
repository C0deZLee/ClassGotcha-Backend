import views
from django.conf.urls import url
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token, verify_jwt_token
from rest_framework.routers import DefaultRouter

# router = DefaultRouter()
# router.register(r'', views.AccountViewSet)
# urlpatterns = router.urls

account_register = views.AccountViewSet.as_view({
	'post': 'create'
})

account_list = views.AccountViewSet.as_view({
	'get': 'list'
})

account_detail = views.AccountViewSet.as_view({
	'get': 'retrieve',
	'put': 'update',
	'delete': 'remove',
})

account_avatar = views.AccountViewSet.as_view({
	'post': 'avatar'
})


urlpatterns = [
	url(r'auth-token/$', obtain_jwt_token),
	url(r'auth-refresh/$', refresh_jwt_token),
	url(r'auth-verify/$', verify_jwt_token),

	# url(r'upload/$', views.AccountViewSet.avatar),
	url(r'register/$', account_register, name='register'),
	# url(r'')
	# url(r'(?P<pk>[0-9]+)/$', views.AccountBasic.as_view()),
	# url(r'(?P<pk>[0-9]+)/detail$', views.AccountDetail.as_view()),
]
