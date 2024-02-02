from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import HttpResponse

# Create your views here.



def home(request):
    return render(request,'student/home.html',{})

def about(request):
    return render(request,'student/about.html',{})
