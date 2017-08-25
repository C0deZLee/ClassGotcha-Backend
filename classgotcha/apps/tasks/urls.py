import views
from django.conf.urls import url

task_detail = views.TaskViewSet.as_view({
	'post': 'add',
	'put': 'update',
	'delete': 'delete'
})

task_remove = views.TaskViewSet.as_view({
	'delete': 'remove'
})

urlpatterns = [
	url(r'^(?P<pk>[0-9]+)/$', task_detail, name='task-detail'),
	url(r'^(?P<pk>[0-9]+)/remove/$', task_remove, name='task-remove'),
]
