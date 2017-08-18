import views
from django.conf.urls import url

task_detail = views.TaskViewSet.as_view({
	'put': 'update',
	'delete': 'delete'
})

urlpatterns = [
	url(r'^(?P<pk>[0-9]+)/$', task_detail, name='task-detail'),
]
