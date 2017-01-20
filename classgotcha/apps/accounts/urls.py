import views
from django.conf.urls import url
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token, verify_jwt_token
from rest_framework.routers import DefaultRouter

# router = DefaultRouter()
# router.register(r'', views.AccountViewSet)
# urlpatterns = router.urls


account_reset_password = views.AccountViewSet.as_view({'post': 'reset_password'})

# account_list = views.AccountViewSet.as_view({'get': 'list'})

account_detail = views.AccountViewSet.as_view({
	'get': 'retrieve',
	'put': 'update',
	'delete': 'destroy'
})

account_friends = views.AccountViewSet.as_view({
	'get': 'friends',
})

account_add_friends = views.AccountViewSet.as_view({
	'post': 'friends',
	'delete': 'friends'
})

account_me = views.AccountViewSet.as_view({
	'get': 'me',
})

account_classrooms = views.AccountViewSet.as_view({
	'get': 'classrooms'
})

account_add_classrooms = views.AccountViewSet.as_view({
	'post': 'classrooms',
	'delete': 'classrooms'
})

account_notes = views.AccountViewSet.as_view({
	'get': 'notes'
})

account_moments = views.AccountViewSet.as_view({
	'get': 'moments'
})

account_rooms = views.AccountViewSet.as_view({
	'get': 'rooms'
})

urlpatterns = [
	url(r'friends/(?P<pk>[0-9]+)/$', account_add_friends, name='add_friend'),
	url(r'moments/(?P<page>[0-9]+)/$', account_moments, name='add_moments'),
	url(r'classrooms/(?P<pk>[0-9]+)/$', account_add_classrooms, name='add_classroom'),
	url(r'(?P<pk>[0-9]+)/$', account_detail, name='detail'),

	url(r'avatar/$', views.account_avatar, name='avatar'),
	url(r'classrooms/$', account_classrooms, name='user-classrooms'),
	url(r'friends/$', account_friends, name='friends'),
	url(r'login/$', obtain_jwt_token),
	url(r'login-refresh/$', refresh_jwt_token),
	url(r'login-verify/$', verify_jwt_token),
	url(r'register/$', views.account_register, name='register'),
	url(r'reset/$', account_reset_password, name='reset_pass'),
	url(r'notes/$', account_notes, name='user-notes'),
	url(r'moments/$', account_moments, name='user-moments'),
	url(r'chatrooms/$', account_rooms, name='user-chatrooms'),

	# url(r'all/$', account_list, name='all'),
	url(r'me/$', account_me, name='me'),
]
