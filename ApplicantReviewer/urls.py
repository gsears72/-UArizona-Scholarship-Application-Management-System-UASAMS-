from django.urls import path, include
from . import views

urlpatterns = [
    path('ARhome', views.ARhome, name='ARhome'),
    path('ViewScholarshipAR', views.ARhome, name='ViewScholarshipAR')
]