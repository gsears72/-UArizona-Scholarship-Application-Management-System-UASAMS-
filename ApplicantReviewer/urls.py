from django.urls import path, include
from . import views

urlpatterns = [
    path('ARhome', views.ARhome, name='ARhome'),
    path('ViewScholarshipsAR', views.ViewScholarshipsAR, name='ViewScholarshipsAR'),
    path('SearchApplicants', views.SearchApplicants, name='SearchApplicants'),
    path('MyReviewedApps', views.MyReviewedApps, name='MyReviewedApps'),
    path('Approved', views.Approved, name='Approved'),
    path ('ViewScholarshipApplicants/<int:scholarship_id>/', views.ViewScholarshipApplicants, name='ViewScholarshipApplicants'),
    path('ReviewApplication/<int:application_id>/<int:scholarship_id>/', views.ViewScholarshipApplicants, name='ReviewApplication')
]