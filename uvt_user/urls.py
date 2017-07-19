from django.conf.urls import include, url
from .views import *

urlpatterns = [
    url(r'^$', manage, name='manage'),
    url(r'^student/$', manage_student, name='manage_student'),
    url(r'^employee/$', manage_employee, name='manage_employee'),
    url(r'^student/([^/]+)/$', student_details, name='student_details'),
    url(r'^employee/([^/]+)/$', employee_details, name='employee_details'),
]
