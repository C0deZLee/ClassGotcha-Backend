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
urlpatterns = [
	url(r'moment/(?P<pk>[0-9]+)/comment/$', moment_comment, name='moment-comment'),
	url(r'moment/(?P<pk>[0-9]+)/like/$', moment_like, name='moment-like'),
	url(r'moment/(?P<pk>[0-9]+)/solve/$', moment_detail, name='moment-detail'),
	url(r'moment/(?P<pk>[0-9]+)/$', moment_detail, name='moment-detail'),

]
