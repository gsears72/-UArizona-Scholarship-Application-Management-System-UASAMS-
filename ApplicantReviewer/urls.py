from django.urls import path, include
from . import views

urlpatterns = [
    path('ARhome', views.ARhome, name='ARhome'),
    path('ViewScholarshipsAR', views.ViewScholarshipsAR, name='ViewScholarshipsAR'),
    path('SearchApplicants', views.SearchApplicants, name='SearchApplicants'),
    path('MyReviewedApps', views.MyReviewedApps, name='MyReviewedApps'),
    path('ARApproved', views.ARApproved, name='ARApproved'),
    path('ViewApplicants/<int:scholarship_id>/', views.ViewApplicants, name='ViewApplicants'),
    path('ViewEligibleApplicants/<int:scholarship_id>/', views.ViewEligibleApplicants, name='ViewEligibleApplicants'),
    path('ReviewApplication/<int:application_id>/<int:scholarship_id>/', views.ReviewApplication, name='ReviewApplication'),
    path('application_list', views.application_list, name='application_list'),
    path('scholarship_list_AR', views.scholarship_list_AR, name='scholarship_list_AR'),
    path('review_submitAR/<int:application_id>/', views.review_submitAR, name='review_submitAR'),
    path('reports', views.ARreports, name='reports'),
    path('ReviewConfirmation', views.ReviewConfirmation, name='ReviewConfirmation')
]