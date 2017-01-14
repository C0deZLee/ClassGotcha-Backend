import views
from django.conf.urls import url

classroom_detail = views.ClassroomViewSet.as_view({
	'get': 'retrieve',
	'put': 'update',
	'post': 'syllabus',
	'option': 'syllabus'
})
# TODO paganation
classroom_all = views.ClassroomViewSet.as_view({
	'get': 'list'
})

classroom_notes = views.ClassroomViewSet.as_view({
	'get': 'notes',
	'post': 'notes'
})

classroom_moments = views.ClassroomViewSet.as_view({
	'get': 'recent_moments'
})

classroom_tasks = views.ClassroomViewSet.as_view({
	'get': 'tasks',
	'post': 'tasks'
})

classroom_students = views.ClassroomViewSet.as_view({
	'get': 'students'
})

urlpatterns = [
	url(r'(?P<pk>[0-9]+)/notes/$', classroom_notes, name='classroom-notes'),
	url(r'(?P<pk>[0-9]+)/tasks/$', classroom_tasks, name='classroom-tasks'),
	url(r'(?P<pk>[0-9]+)/students/$', classroom_students, name='classroom-students'),
	url(r'(?P<pk>[0-9]+)/moments/$', classroom_moments, name='classroom-moments'),
	url(r'(?P<pk>[0-9]+)/$', classroom_detail, name='classroom-detail'),
	url(r'all/$', classroom_all, name='classroom-all'),

]

# classroom/all
# classroom/<id>/students
# classroom/<id>/tasks
# classroom/<id>/
