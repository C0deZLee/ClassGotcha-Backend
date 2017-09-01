import views
from django.conf.urls import url
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token, verify_jwt_token

account_get_iCal_token = views.AccountViewSet.as_view({
	'get': 'get_iCal_token'
})

account_change_password = views.AccountViewSet.as_view({
	'post': 'change_password'
})

account_detail = views.AccountViewSet.as_view({
	'get'   : 'retrieve',
	'delete': 'destroy'
})

account_friends = views.AccountViewSet.as_view({
	'get': 'friends',
})

account_add_friends = views.AccountViewSet.as_view({
	'post'  : 'friends',
	'put'   : 'friends',
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
	'post'  : 'classrooms',
	'delete': 'classrooms'
})

account_chatrooms = views.AccountViewSet.as_view({
	'get': 'rooms'
})

account_add_chatrooms = views.AccountViewSet.as_view({
	'post'  : 'rooms',
	'delete': 'rooms'
})

account_notes = views.AccountViewSet.as_view({
	'get': 'notes'
})

account_moments = views.AccountViewSet.as_view({
	'get' : 'moments',
})

add_delete_moments = views.AccountViewSet.as_view({
	'post'  : 'moments',
	'delete': 'moments'
})

account_tasks = views.AccountViewSet.as_view({
	'get' : 'tasks',
	'post': 'tasks'
})

account_tasks_edit = views.AccountViewSet.as_view({
	'put': 'tasks',
})

account_explore = views.AccountViewSet.as_view({
	'get': 'explore_friends'
})

account_search = views.AccountViewSet.as_view({
	'post': 'search'
})

account_plan = views.AccountViewSet.as_view({
	'get': 'study_plan'
})

professor_detail = views.ProfessorViewSet.as_view({
	'get': 'retrieve',
	'put': 'update'
})

professor_comments = views.ProfessorViewSet.as_view({
	'get' : 'comments',
	'post': 'comments'
})

urlpatterns = [
	url(r'^avatar/change/$', views.account_avatar, name='user-avatar'),

	url(r'^classrooms/(?P<pk>[0-9]+)/$', account_add_classrooms, name='add-classroom'),
	url(r'^chatrooms/(?P<pk>[0-9]+)/$', account_add_chatrooms, name='add-chatrooms'),

	url(r'^get_ical_token/$', account_get_iCal_token, name='get-ical-token'),
	url(r'^(?P<token>[A-z0-9]+)/feed.ics$', views.ical_feed_view, name='user-calendar-feed'),

	url(r'^(?P<pk>[0-9]+)/$', account_detail, name='user-detail'),
	url(r'^(?P<account_pk>[0-9]+)/moments/$', account_moments, name='user-detail-moments'),

	url(r'^moments/$', account_moments, name='my-moments'),
	url(r'^moments/(?P<moment_pk>[0-9]+)/$', account_moments, name='add-delete-moment'),

	url(r'^classrooms/$', account_classrooms, name='user-classrooms'),
	url(r'^chatrooms/$', account_chatrooms, name='user-chatrooms'),

	url(r'^friends/$', account_friends, name='user-friends'),
	url(r'^friends/(?P<pk>[0-9]+)/$', account_add_friends, name='add-friend'),

	url(r'^pending-friends/$', account_pending_friends, name='user-pending-friends'),
	url(r'^recommend-friends/$', account_explore, name='user-explore-friends'),
	url(r'^search/$', account_search, name='user-search'),
	url(r'^login/$', obtain_jwt_token),
	url(r'^login-refresh/$', refresh_jwt_token),
	url(r'^login-verify/$', verify_jwt_token),

	url(r'^register/$', views.account_register, name='user-register'),

	url(r'^verify/$', views.email_verify, name='email-verify-request'),
	url(r'^verify/(?P<token>[A-z0-9\-]+)/$', views.email_verify, name='email-verifying'),

	url(r'^notes/$', account_notes, name='user-notes'),

	url(r'^tasks/$', account_tasks, name='user-tasks'),
	url(r'^tasks/(?P<pk>[0-9]+)$', account_tasks_edit, name='user-tasks-edit'),

	url(r'^plan/$', account_plan, name='user-study-plan'),

	url(r'^forget/$', views.forget_password, name='user-forget-password-gettoken'),
	url(r'^forget/(?P<token>[A-z0-9\-]+)/$', views.forget_password, name='user-forget-password'),
	url(r'^passchange/$', account_change_password, name='change-pass'),

	url(r'^me/$', account_me, name='me'),

	url(r'^professor/(?P<pk>[0-9]+)/$', professor_detail, name='professor-detail'),
	url(r'^professor/(?P<pk>[0-9]+)/comment/$', professor_comments, name='professor-comments'),

]
