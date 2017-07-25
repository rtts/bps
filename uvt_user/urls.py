from django.conf.urls import include, url
from .views import *

urlpatterns = [
    url(r'^$', manage, name='manage'),
    url(r'^user/$', lookup_user, name='lookup_user'),
    url(r'^user/([^/]+)/$', user_details_readonly, name='user_details_readonly'),
    url(r'^user/([^/]+)/change/$', user_details, name='user_details'),
]
