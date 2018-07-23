from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from management import views

urlpatterns = [
    url(r'^management/$', views.assets_list),
    url(r'^management/(?P<pk>[0-9]+)/$', views.asset_detail),
]

urlpatterns = format_suffix_patterns(urlpatterns)