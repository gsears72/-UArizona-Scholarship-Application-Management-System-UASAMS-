from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='SDhome'),
    path('EditScholarshipView/<int:scholarship_id>/', views.viewMore, name='EditScholarshipView'),
]