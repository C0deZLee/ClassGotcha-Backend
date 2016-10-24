import views
from django.conf.urls import url

urlpatterns = [
	url(r'all$', views.GroupList.as_view(), name='group-list'),
	url(r'me$', views.MyCreatedGroupList.as_view(), name='my-group-list'),
	url(r'me/create$', views.MyCreatedGroupList.as_view(), name='my-created-group-list'),
	url(r'class/(?P<pk>[0-9]+)$', views.ClassGroupsList.as_view(), name='class-group-list'),
	url(r'(?P<pk>[0-9]+)/members', views.GroupMembersList.as_view(), name='group-members-list'),
	url(r'(?P<pk>[0-9]+)/creator', views.GroupCreatorList.as_view(), name='group-creator')
]
