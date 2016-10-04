from django.conf.urls import patterns, include, url

import .views


urlpatterns = [
    url(r"^account/signup/$", views.SignupView.as_view(), name="account_signup"),
    url(r"^account/", include("account.urls")),
]
