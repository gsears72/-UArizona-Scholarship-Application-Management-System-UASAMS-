from django.urls import path
from . import views

urlpatterns = [
    path('login_user', views.login_user, name='login'),
    path('logout_user', views.logout_user, name='logout'),

    path('student_register', views.studentRegister, name='student_register'),
    path('scholorship_adminstrator_register', views.scholorshipadminstratoRegister, name='scholorship_adminstrator_register'),
    path('scholorship_donor_register', views.scholorshipdonorregisterRegister, name='scholorship_donor_register'),
    path('applicant_reviewer_register', views.applicantreviewerRegister, name='applicant_reviewer_register'),

]