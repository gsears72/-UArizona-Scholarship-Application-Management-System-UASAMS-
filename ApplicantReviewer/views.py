from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import get_list_or_404

from ScholarshipDonor.models import Scholarship
from SFWEScholarships.models import Application
from Student.models import Student

def ARhome(request):
    return render(request,'ARhome.html',{})

def ViewScholarshipsAR(request):
    scholarships_object = Scholarship.objects.all()
    context = {'scholarships_object' : scholarships_object}
    return render(request,'ViewScholarshipsAR.html', context)

def SearchApplicants(request):
    return render(request,'SearchApplicants.html',{})

def MyReviewedApps(request):
    return render(request,'MyReviewedApps.html',{})

def Approved(request):
    return render(request,'Approved.html',{})

def ViewScholarshipApplicants(request, scholarship_id):
    currScholarship = scholarship_id
    application_object = Application.objects.all()
    return render(request,'ViewScholarshipApplicants.html',{'scholarship': currScholarship, 'application': application_object})