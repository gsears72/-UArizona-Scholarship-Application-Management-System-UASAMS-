from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='Shome'),
    path('', views.ViewScholarships, name='SViewScholarships'),
    path('', views.ViewProfile, name= 'SViewProfile'),
    path('', views.CheckAppStatus, name= 'SCheckAppStatus'),

]