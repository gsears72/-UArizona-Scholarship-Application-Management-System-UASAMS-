from django.urls import path, include
from Login import views

urlpatterns = [
    path('', views.login_user, name='home'),
]