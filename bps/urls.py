import django.contrib.auth.views
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.conf import settings
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
import autodidact.urls
import uvt_user.urls
import cas.views

urlpatterns = [
    url(r'^login/$',cas.views.login, name='login'),
    url(r'^logout/$',cas.views.logout, name='logout'),
    url(r'^admin/login/$', cas.views.login, name='admin:login'),
    url(r'^admin/', admin.site.urls),
    url(r'^manage/', include(uvt_user.urls)),
    url(r'^', include(autodidact.urls)),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
