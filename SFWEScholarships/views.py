from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import HttpResponse

# Create your views here.



def home(request):
    return render(request,'home.html',{})

def about(request):
    return render(request,'about.html',{})

def application_form(request):
    return render(request,'application_form.html',{})
