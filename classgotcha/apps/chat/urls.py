
from django.conf.urls import patterns, url


urlpatterns = patterns("classgotcha.apps.chat.views",
    url("^$", "rooms", name="rooms"),
    url("^create/$", "create", name="create"),
    url("^system_message/$", "system_message", name="system_message"),
    url("^(?P<slug>.*)$", "room", name="room"),
)
