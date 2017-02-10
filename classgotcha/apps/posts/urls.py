import views
from django.conf.urls import url

moment_detail = views.MomentViewSet.as_view({
	'get': 'retrieve',
})
moment_solve = views.MomentViewSet.as_view({
	'post': 'solve'
})
moment_comment = views.MomentViewSet.as_view({
	'post': 'comment'
})
moment_like = views.MomentViewSet.as_view({
	'post': 'like'
})
moment_report = views.MomentViewSet.as_view({
	'put': 'report'
})
post_list = views.PostViewSet.as_view({
	'get': 'list',
	'post': 'create'
})
post_detail = views.PostViewSet.as_view({
	'get': 'retrieve',
	'put': 'vote'
})
post_comment = views.PostViewSet.as_view({
	'post': 'comment'
})
urlpatterns = [
	url(r'^moment/(?P<pk>[0-9]+)/comment/$', moment_comment, name='moment-comment'),
	url(r'^moment/(?P<pk>[0-9]+)/like/$', moment_like, name='moment-like'),
	url(r'^moment/(?P<pk>[0-9]+)/solve/$', moment_solve, name='moment-detail'),
	url(r'^moment/(?P<pk>[0-9]+)/report/$', moment_report, name='moment-report'),
	url(r'^moment/(?P<pk>[0-9]+)/$', moment_detail, name='moment-detail'),
	url(r'^post/$', post_list, name='post-list'),
	url(r'^post/(?P<pk>[0-9]+)/$', post_detail, name='post-detail'),
	url(r'^post/(?P<pk>[0-9]+)/comment/$', post_comment, name='post-comment'),

]
