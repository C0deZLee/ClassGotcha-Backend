import views
from django.conf.urls import url

urlpatterns = [
    url(r'^init/$', views.action_init, name='action-init'),
]
