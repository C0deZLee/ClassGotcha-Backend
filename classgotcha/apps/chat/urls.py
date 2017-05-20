import views
from django.conf.urls import url
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token, verify_jwt_token

creat_private_group_chat = views.ChatViewSet.as_view({

	'post':'creat_private_group_chat' 


	})


urlpatterns = [

	url(r'^chatrooms/creat_private_group_chat$',creat_private_group_chat,name = 'creat_private_group')



]