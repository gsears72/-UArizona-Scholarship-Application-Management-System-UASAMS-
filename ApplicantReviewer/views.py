from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import HttpResponse

# Create your views here.

def ARhome(request):
    return render(request,'ARhome.html',{})

def ViewScholarshipsAR(request):
    return render(request,'ViewScholarshipsAR.html',{})

def SearchApplicants(request):
    return render(request,'SearchApplicants.html',{})

def MyReviewedApps(request):
    return render(request,'MyReviewedApps.html',{})

def Approved(request):
    return render(request,'Approved.html',{})

def ViewScholarshipApplicants(request):
    return render(request,'ViewScholarshipApplicants.html',{})