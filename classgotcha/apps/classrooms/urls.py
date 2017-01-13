import views
from django.conf.urls import url

classroom_detail = views.ClassroomViewSet.as_view({
	'get': 'retrieve',
	'put': 'update',
	'post': 'syllabus',
	'option': 'syllabus'
})

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

urlpatterns = [
	# url(r'all$', views.MyClassrooms.as_view(), name='moment-list'),
	# visitor can only get the basic info of our classrooms
	# url(r'(?P<pk>[0-9]+)/visitor/$', views.BasicClassroomSerializer.as_view(), name='classroom-basic'),
	# student can have full access
	url(r'(?P<pk>[0-9]+)/notes/$', classroom_notes, name='classroom-notes'),
	url(r'(?P<pk>[0-9]+)/moments/$', classroom_moments, name='classroom-moments'),
	url(r'(?P<pk>[0-9]+)/$', classroom_detail, name='classroom-detail'),
	url(r'all/$', classroom_all, name='classroom-all'),

]

# classroom/all
# classroom/<id>/students
# classroom/<id>/tasks
# classroom/<id>/
