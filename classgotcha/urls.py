"""classgotcha URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from classgotcha.apps.accounts import urls as accounts_urls
from classgotcha.apps.classrooms import urls as classroom_urls
from classgotcha.apps.moments import urls as moments_urls
from django.conf.urls import include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = [
    url(r'^accounts/', include(accounts_urls)),
    url(r'^moments/', include(moments_urls)),
    url(r'^classrooms/', include(classroom_urls)),
    url(r'^admin/', admin.site.urls),
    url(r'^apidocs/', include('rest_framework_docs.urls'))
    # url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
