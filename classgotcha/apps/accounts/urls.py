import views
from django.conf.urls import url
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token, verify_jwt_token

account_reset_password = views.AccountViewSet.as_view({
	'post': 'reset_password'
})

account_detail = views.AccountViewSet.as_view({
	'get': 'retrieve',
	'delete': 'destroy'
})

account_friends = views.AccountViewSet.as_view({
	'get': 'friends',
})

account_add_friends = views.AccountViewSet.as_view({
	'post': 'friends',
	'put': 'friends',
	'delete': 'friends'
})

account_pending_friends = views.AccountViewSet.as_view({
	'get': 'pending_friends'
})

account_me = views.AccountViewSet.as_view({
	'get': 'me',
	'put': 'me'
})

account_classrooms = views.AccountViewSet.as_view({
	'get': 'classrooms'
})

account_add_classrooms = views.AccountViewSet.as_view({
	'post': 'classrooms',
	'delete': 'classrooms'
})

account_chatrooms = views.AccountViewSet.as_view({
	'get': 'rooms'
})

account_add_chatrooms = views.AccountViewSet.as_view({
	'post': 'rooms',
	'delete': 'rooms'
})

account_notes = views.AccountViewSet.as_view({
	'get': 'notes'
})

account_moments = views.AccountViewSet.as_view({
	'get': 'moments',
	'put': 'moments',
	'post': 'moments'
})

account_add_moments = views.AccountViewSet.as_view({
	'post': 'moments',
	'delete': 'moments'
})
account_tasks = views.AccountViewSet.as_view({
	'get': 'tasks',
	'put': 'tasks',
	'post': 'tasks',
	'delete': 'tasks'
})

account_freetime = views.AccountViewSet.as_view({
	'get': 'freetime'
})

professor_detail = views.ProfessorViewSet.as_view({
	'get': 'retrieve',
	'put': 'update'
})

professor_comments = views.ProfessorViewSet.as_view({
	'get': 'comments',
	'post': 'comments'
})

urlpatterns = [
	url(r'^friends/(?P<pk>[0-9]+)/$', account_add_friends, name='add-friend'),
	url(r'^moments/(?P<pk>[0-9]+)/$', account_add_moments, name='add-moment'),
	url(r'^classrooms/(?P<pk>[0-9]+)/$', account_add_classrooms, name='add-classroom'),
	url(r'^chatrooms/(?P<pk>[0-9]+)/$', account_add_chatrooms, name='add-chatroom'),

	url(r'^(?P<pk>[0-9]+)/$', account_detail, name='user-detail'),

	url(r'^avatar/$', views.account_avatar, name='user-avatar'),
	url(r'^classrooms/$', account_classrooms, name='user-classrooms'),
	url(r'^chatrooms/$', account_chatrooms, name='user-chatrooms'),
	url(r'^friends/$', account_friends, name='uer-friends'),
	url(r'^pending-friends/$', account_pending_friends, name='user-pending-friends'),
	url(r'^login/$', obtain_jwt_token),
	url(r'^login-refresh/$', refresh_jwt_token),
	url(r'^login-verify/$', verify_jwt_token),
	url(r'^register/$', views.account_register, name='register'),
	url(r'^reset/$', account_reset_password, name='reset-pass'),
	url(r'^notes/$', account_notes, name='user-notes'),
	url(r'^moments/$', account_moments, name='user-moments'),
	url(r'^tasks/$', account_tasks, name='user-tasks'),
	url(r'^freetime/$', account_freetime, name='freetime'),

	url(r'^me/$', account_me, name='me'),

	url(r'^professor/(?P<pk>[0-9]+)/$', professor_detail, name='professor-detail'),
	url(r'^professor/(?P<pk>[0-9]+)/comment/$', professor_comments, name='professor-comments'),

]
