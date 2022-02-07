from django.urls import re_path
from loadImage.views import ViewListImg
from loadImage.views import ViewDetailImg

urlpatterns = [
    re_path(r'^img/$', ViewListImg.as_view()),
    re_path(r'^img/(?P<pk>\d+)$', ViewDetailImg.as_view())
]
