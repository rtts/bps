from django.urls import path, include
from .views import *

urlpatterns = [
    path('tag/<slug:slug>/', tag, name='tag'),
    path('course/<slug:slug>/', course, name='course'),
    path('course/<slug:slug>/session/<int:session_nr>/', session, name='session'),
    path('course/<slug:slug>/session/<int:session_nr>/assignment/<int:assignment_nr>/', assignment, name='assignment'),
    path('course/<slug:slug>/add_session/', add_session, name='add_session'),
    path('course/<slug:slug>/session/<int:session_nr>/add_assignment/', add_assignment, name='add_assignment'),
    path('course/<slug:slug>/session/<int:session_nr>/assignment/<int:assignment_nr>/add_step/', add_step, name='add_step'),

    path('', include('cms.urls', namespace='cms')),
]
