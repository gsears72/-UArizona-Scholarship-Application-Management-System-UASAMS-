from django.urls import path, include
from . import views

urlpatterns = [
    path('ARhome', views.ARhome, name='ARhome'),
    path('ViewScholarshipsAR', views.ViewScholarshipsAR, name='ViewScholarshipsAR'),
    path('SearchApplicants', views.SearchApplicants, name='SearchApplicants'),
    path('MyReviewedApps', views.MyReviewedApps, name='MyReviewedApps'),
    path('Approved', views.Approved, name='Approved'),
    path('ViewApplicants/<int:scholarship_id>/', views.ViewApplicants, name='ViewApplicants'),
    path('ViewEligibleApplicants/<int:scholarship_id>/', views.ViewEligibleApplicants, name='ViewEligibleApplicants'),
    path('ReviewApplication/<int:application_id>/<int:scholarship_id>/', views.ReviewApplication, name='ReviewApplication'),
    path('application-list', views.application_list, name='application_list'),
    path('scholarship-list', views.scholarship_list, name='scholarship_list'),
    path('review-submit/<int:application_id>/', views.review_submit, name='review_submit')
]