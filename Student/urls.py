from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='Shome'),
    path('SViewScholarships', views.ViewScholarships, name='SViewScholarships'),
    path('SViewProfile', views.ViewProfile, name= 'SViewProfile'),
    path('SCheckAppStatus', views.CheckAppStatus, name= 'SCheckAppStatus'),
    path('SViewScholarshipInfo/<int:scholarship_id>/', views.ViewScholarshipInfo, name= 'SViewScholarshipInfo'),
    path('applicationForm/<int:scholarship_id>/', views.ViewApplication, name= 'applicationForm'),
    path('SViewEligableScholarships', views.ViewEligableScholarships, name= 'SViewEligableScholarships'),
    path('createApplication/<int:scholarship_id>/', views.createApplication, name='createApplication'),
    path('SeditProfile', views.editProfile, name= 'SeditProfile'),
]