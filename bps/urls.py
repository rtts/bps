from django.contrib import admin
from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib.auth.views import LoginView, LogoutView

import autodidact.urls
import uvt_user.urls

admin.site.site_header = 'BPS Admin'
admin.site.site_title = 'BPS Admin'

if settings.CAS_SERVER_URL:
    import cas.views
    login = cas.views.login
    logout = cas.views.logout
else:
    login = LoginView.as_view()
    logout = LogoutView.as_view()

urlpatterns = []

if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += [
    url(r'^login/$', login, name='login'),
    url(r'^logout/$', logout, name='logout'),
    url(r'^admin/login/$', login),
    url(r'^admin/logout/$', logout),
    url(r'^admin/', admin.site.urls),
    url(r'^manage/', include(uvt_user.urls)),
    url(r'^', include(autodidact.urls)),
]
