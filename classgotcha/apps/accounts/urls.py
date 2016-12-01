import views
from django.conf.urls import url
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token, verify_jwt_token


urlpatterns = [
	url(r'register/$', views.AccountCreate.as_view(), name='register'),
	url(r'auth/$', obtain_jwt_token),
	url(r'auth-refresh/$', refresh_jwt_token),
	url(r'auth-verify/$', verify_jwt_token),
	url(r'(?P<pk>[0-9]+)/$', views.AccountBasic.as_view()),
	url(r'(?P<pk>[0-9]+)/detail$', views.AccountDetail.as_view())
]
