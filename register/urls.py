from django.urls import re_path

from register.views import RegisterView

urlpatterns = [
    re_path(r'^registro/', RegisterView.as_view())
]