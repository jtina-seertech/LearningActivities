from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    url(r'rest-auth/', include('rest_auth.urls')),
    url(r'^assets/$', views.assets_list),
    url(r'^assets/(?P<pk>[0-9]+)/$', views.asset_detail),
    url(r'^status_list/$', views.status_list),
    url(r'^borrower_list/$', views.asset_borrower_list),
]

urlpatterns = format_suffix_patterns(urlpatterns)