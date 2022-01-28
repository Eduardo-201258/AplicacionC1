from django.urls import re_path

from primerComponente.views import PrimerViewList

urlpatterns = [
    re_path(r'^lista/$', PrimerViewList.as_view())
]
