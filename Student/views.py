from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request,'Shome.html', {})

def ViewScholarships(request):
    return render(request, 'SViewScholarships.html', {})

def ViewProfile(request):
    return render(request, 'SViewProfile.html', {})

def CheckAppStatus(request):
    return render(request, 'SCheckAppStatus.html', {})