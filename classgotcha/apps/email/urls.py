import views
from django.conf.urls import url

urlpatterns = [
    url(r'^test/$', views.test, name='test'),
]
