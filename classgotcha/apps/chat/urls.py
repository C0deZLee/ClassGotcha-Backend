import views
from django.conf.urls import url

urlpatterns = [

	# url(r"^$", views.rooms, name="rooms"),
	# url(r"^system_message/$", views.system_message, name="system_message"),
	url(r'^$', views.about, name='about'),
	url(r'^new/$', views.new_room, name='new_room'),
	url(r"^(?P<label>[\w-]{,50})/$", views.chat_room, name="room"),
]
