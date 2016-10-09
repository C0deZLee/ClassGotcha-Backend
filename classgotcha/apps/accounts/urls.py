import views
from django.conf.urls import url

urlpatterns = [
	url(r'$', views.AccountList.as_view(), name='account-list'),
	url(r'(?P<pk>[0-9]+)/$', views.AccountDetail.as_view())
]
