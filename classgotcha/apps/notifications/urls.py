import views
from django.conf.urls import url

notification_fetch = views.NotificationViewSet.as_view({
	'get': 'fetch'
})

notification_read = views.NotificationViewSet.as_view({
	'post': 'read'
})

urlpatterns = [
	url(r'^fetch/$', notification_fetch, name='notification-fetch'),
	url(r'^read/(?P<pk>[0-9]+)/$', notification_read, name='notification-read'),
]
