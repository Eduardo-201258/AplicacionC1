from django import urls
from django.urls import URLPattern, path, re_path
from django.conf.urls import include

from login.views import LoginAuth

urlpatterns = [
    re_path(r'^', LoginAuth.as_view()),
]
