from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import HttpResponse
from ScholarshipDonor.tempData import tempData
from ScholarshipDonor.models import Scholarship
# Create your views here.

def home(request):
    return render(request,'Shome.html', {})

def ViewScholarships(request):
    scholarships_object = Scholarship.objects.all()
    context = {'scholarships_object' : scholarships_object}
    return render(request, 'SViewScholarships.html', context)

def ViewProfile(request):
    return render(request, 'SViewProfile.html', {})

def CheckAppStatus(request):
    application_object = Application.objects.all()
    context = {'application_object' : application_object}
    return render(request, 'SCheckAppStatus.html',context)

def ViewScholarshipInfo(request):
    return render(request, 'SViewScholarshipInfo.html', {})

