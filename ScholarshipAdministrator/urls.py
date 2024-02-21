from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='SAhome'),
    path('create-scholarship', views.create_scholarship, name='create_scholarship'),
    path('scholarship-list', views.scholarship_list, name='scholarship_list'),
    path('edit-scholarship/<scholarship_name>/', views.edit_scholarship, name='edit_scholarship'),
    path('delete-scholarship/<scholarship_name>/', views.delete_scholarship, name='delete_scholarship'),    
    path('create-scholarship-submit', views.create_scholarship_submit, name='create_scholarship_submit')

]