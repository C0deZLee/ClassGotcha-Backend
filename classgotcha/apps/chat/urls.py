import views
from django.conf.urls import  url


urlpatterns = [
    
    url(r"^$", views.rooms, name="rooms"),
    url(r"^system_message/$", views.system_message, name="system_message"),
    url(r"^(?P<slug>.*)$", views.room, name="room"),
]
