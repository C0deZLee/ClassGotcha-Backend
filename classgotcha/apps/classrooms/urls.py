import views
from django.conf.urls import url

classroom_detail = views.ClassroomViewSet.as_view({
	'get': 'retrieve',
	'put': 'update',
	'post': 'syllabus',
	# 'option': 'syllabus'
})

classroom_notes = views.ClassroomViewSet.as_view({
	'get': 'notes',
	'post': 'notes'
})

classroom_moments = views.ClassroomViewSet.as_view({
	'get': 'moments'
})

classroom_tasks = views.ClassroomViewSet.as_view({
	'get': 'tasks',
	'post': 'tasks',
})

classroom_students = views.ClassroomViewSet.as_view({
	'get': 'students'
})

classroom_validate = views.ClassroomViewSet.as_view({
	'get': 'validate'
})

classroom_search = views.ClassroomViewSet.as_view({
	'post': 'search'
})

classroom_course_upload = views.ClassroomViewSet.as_view({
	'post': 'upload_course_info'
})

classroom_major_upload = views.ClassroomViewSet.as_view({
	'post': 'upload_major_info'
})

majors_all = views.MajorViewSet.as_view({
	'get': 'list'
})

urlpatterns = [
	url(r'^(?P<pk>[0-9]+)/notes/$', classroom_notes, name='classroom-notes'),
	url(r'^(?P<pk>[0-9]+)/tasks/$', classroom_tasks, name='classroom-tasks'),
	url(r'^(?P<pk>[0-9]+)/students/$', classroom_students, name='classroom-students'),
	url(r'^(?P<pk>[0-9]+)/moments/$', classroom_moments, name='classroom-moments'),
	url(r'^(?P<pk>[0-9]+)/moments/(?P<page>[0-9]+)/$', classroom_moments, name='classroom-moments-page'),
	url(r'^(?P<pk>[0-9]+)/validate/$', classroom_validate, name='classroom-check'),
	url(r'^(?P<pk>[0-9]+)/$', classroom_detail, name='classroom-detail'),
	url(r'^search/$', classroom_search, name='classroom-search'),
	url(r'^majors/$', majors_all, name='major-list'),
	url(r'^course-upload/$', classroom_course_upload, name='classroom-course-upload'),
	url(r'^major-upload/$', classroom_major_upload, name='classroom-major-upload'),
]

# classroom/all
# classroom/<id>/students
# classroom/<id>/tasks
# classroom/<id>/
