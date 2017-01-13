import views
from django.conf.urls import url

moment_detail = views.MomentViewSet.as_view({
	'get': 'retrieve',
	'delete': 'destroy'

})

urlpatterns = [
	url(r'moment/(?P<pk>[0-9]+)/$', moment_detail, name='moment-detail'),
]
