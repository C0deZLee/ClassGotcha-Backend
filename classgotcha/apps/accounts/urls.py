import views
from django.conf.urls import url

urlpatterns = [
	url(r'$', views.AccountList.as_view(), name='account-list'),
	url(r'me$', views.AccountBasic.as_view()),
	url(r'(?P<pk>[0-9]+)/$', views.AccountBasic.as_view()),
	url(r'(?P<pk>[0-9]+)/detail', views.AccountDetail.as_view()),
	url(r'(?P<pk>[0-9]+)/moments$', views.AccountMoments.as_view())
]
