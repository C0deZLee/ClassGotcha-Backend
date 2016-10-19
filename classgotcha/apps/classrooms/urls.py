import views
from django.conf.urls import url

urlpatterns = [
	url(r'$', views.MyClassrooms.as_view(), name='moment-list'),
	# visitor can only get the basic info of our classrooms
	# url(r'(?P<pk>[0-9]+)/visitor/$', views.BasicClassroomSerializer.as_view(), name='classroom-basic'),
	# student can have full access
	url(r'(?P<pk>[0-9]+)/stu/$', views.ClassroomList.as_view(), name='classroom-detail')
]
