import views
from django.conf.urls import url

chatroom_detail = views.ChatRoomViewSet.as_view({
	'get': 'retrieve',
	'post': 'join',
	'delete': 'quit'
})

clatroom_create = views.ChatRoomViewSet.as_view({
	'post': 'create',
})

chatroom_users = views.ChatRoomViewSet.as_view({
	'get': 'users',
})

chatroom_validate = views.ChatRoomViewSet.as_view({
	'get': 'validate'
})

urlpatterns = [
	# url(r"^$", views.rooms, name="rooms"),
	# url(r"^system_message/$", views.system_message, name="system_message"),
	# url(r'^$', views.about, name='about'),
	# url(r'^new/$', views.new_room, name='new_room'),
	# url(r"^(?P<label>[\w-]{,50})/$", views.chat_room, name="room"),


	url(r'(?P<pk>[0-9]+)/validate/$', chatroom_validate, name='chatroom-validate'),
	url(r'(?P<pk>[0-9]+)/users/$', chatroom_users, name='chatroom-users'),
	url(r'(?P<pk>[0-9]+)/$', chatroom_detail, name='chatroom-detail'),
	url(r'$', clatroom_create, name='chatroom-create'),

]
