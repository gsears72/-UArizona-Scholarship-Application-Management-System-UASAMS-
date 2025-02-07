from django.urls import path, include
from . import views
from EventLog.views import generate_StudentDemographicsReport, generate_AvailableScholarshipsReport, generate_ArchivedScholarshipsReport, generate_ScholarshipApplicationReport, generate_AwardedScholarshipReport, generate_ActiveDonorsReport

urlpatterns = [
    path('', views.home, name='SAhome'),
    path('create-scholarship', views.create_scholarship, name='create_scholarship'),
    path('scholarship-list', views.scholarship_list, name='scholarship_list'),
    path('edit-scholarship/<str:scholarship_name>/', views.edit_scholarship, name='edit_scholarship'),
    path('delete-scholarship/<str:scholarship_name>/', views.delete_scholarship_page, name='delete_scholarship'),    
    path('create-scholarship-submit', views.create_scholarship_submit, name='create_scholarship_submit'),
    path('delete-scholarship-db/<str:scholarship_name>/', views.delete_scholarship_db, name='delete_scholarship_db'),
    path('edit-scholarship-db/<str:scholarship_name>/', views.edit_scholarship, name='edit_scholarship_db'),
    path('viewChangeRequest', views.viewChangeRequest, name='viewChangeRequest'),
    path('denyChangeRequest/<int:change_id>/', views.denyChangeRequest, name='denyChangeRequest'),
    path('approveChangeRequest/<int:change_id>/', views.approveChangeRequest, name='approveChangeRequest'),
    path('edit-scholarship-db/<str:scholarship_name>/', views.edit_scholarship, name='edit_scholarship_db'),
    path('application-list/<int:scholarship_id>/', views.application_listy, name = 'application_listy'),
    path('review-application/<int:application_id>/<int:scholarship_id>/', views.review_application, name = 'review_application'),
    path('application-approval/<int:application_id>/<int:scholarship_id>/', views.application_approval, name = 'application_approval'),


    path('Reports', views.Reports, name='Reports'),
    path('generate_StudentDemographicsReport/', generate_StudentDemographicsReport, name='generate_StudentDemographicsReport'),
    path('generate_AvailableScholarshipsReport/', generate_AvailableScholarshipsReport, name='generate_AvailableScholarshipsReport'),
    path('generate_ArchivedScholarshipsReport/', generate_ArchivedScholarshipsReport, name='generate_ArchivedScholarshipsReport'),
    path('generate_ScholarshipApplicationReport/', generate_ScholarshipApplicationReport, name='generate_ScholarshipApplicationReport'),
    path('generate_AwardedScholarshipReport/', generate_AwardedScholarshipReport, name='generate_AwardedScholarshipReport'),
    path('generate_ActiveDonorsReport/', generate_ActiveDonorsReport, name='generate_ActiveDonorsReport'),
]