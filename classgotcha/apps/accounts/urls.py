import views
from django.conf.urls import url

urlpatterns = [
	url(r'accounts/$', views.accounts_list),
	url(r'accounts/(?P<pk>[0-9]+)/$', views.accounts_detail)
]
