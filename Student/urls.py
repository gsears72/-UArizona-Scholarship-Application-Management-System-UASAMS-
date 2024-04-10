from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='Shome'),
    path('SViewScholarships', views.ViewScholarships, name='SViewScholarships'),
    path('SViewProfile', views.ViewProfile, name= 'SViewProfile'),
    path('SCheckAppStatus', views.CheckAppStatus, name= 'SCheckAppStatus'),
    path('SViewScholarshipInfo/<int:scholarship_id>/', views.ViewScholarshipInfo, name= 'SViewScholarshipInfo'),
    path('applicationForm/<int:scholarship_id>/', views.ViewCreateApplication, name= 'applicationForm'),
    path('SViewEligableScholarships', views.ViewEligableScholarships, name= 'SViewEligableScholarships'),
    path('SeditProfile', views.editProfile, name= 'SeditProfile'),
]