import views
from django.conf.urls import url

urlpatterns = [
	url(r'$', views.MomentList.as_view(), name='moment-list'),
	url(r'momentsuser$', views.api_root),
	url(r'(?P<pk>[0-9]+)/$', views.MomentDetail.as_view(), name='moment-detail')
]
