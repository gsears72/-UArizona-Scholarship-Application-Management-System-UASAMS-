from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='Shome'),
    path('SViewScholarships', views.ViewScholarships, name='SViewScholarships'),
    path('SViewProfile', views.ViewProfile, name= 'SViewProfile'),
    path('SCheckAppStatus', views.CheckAppStatus, name= 'SCheckAppStatus'),

]