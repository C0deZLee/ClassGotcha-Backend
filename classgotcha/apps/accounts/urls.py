import views
from django.conf.urls import url

urlpatterns = [
	url(r'me$', views.AccountBasic.as_view()),
	url(r'register', views.register, name='register'),
	url(r'(?P<pk>[0-9]+)/$', views.AccountBasic.as_view()),
	url(r'(?P<pk>[0-9]+)/detail', views.AccountDetail.as_view())
]
