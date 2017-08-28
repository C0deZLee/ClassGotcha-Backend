import views
from django.conf.urls import url

chatroom = views.ChatroomViewSet.as_view({
	'get': 'retrieve',
	'post': 'create'
})

chatroom_join = views.ChatroomViewSet.as_view({
	'post': 'join',
})

urlpatterns = [
	url(r'$', chatroom, name='chatrooms'),
	url(r'join/$', chatroom_join, name='chatrooms-join')
]
