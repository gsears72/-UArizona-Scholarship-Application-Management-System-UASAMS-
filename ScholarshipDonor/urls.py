from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='SDhome'),
    path('EditScholarshipView/<int:scholarship_id>/', views.viewMore, name='EditScholarshipView'),
    path('ViewApplicantsSD/<int:scholarship_id>/', views.ViewApplicantsSD, name='ViewApplicantsSD'),
    path('ViewEligibleApplicantsSD/<int:scholarship_id>/', views.ViewEligibleApplicantsSD, name='ViewEligibleApplicantsSD'),
    path('createChangeRequest/<int:scholarship_id>/', views.createChangeRequest, name='createChangeRequest'),
    path('ReviewApplication/<int:application_id>/<int:scholarship_id>/', views.ReviewApplication, name='ReviewApplication'),
]