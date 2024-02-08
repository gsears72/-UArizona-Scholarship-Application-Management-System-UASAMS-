from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import HttpResponse
from .tempData import tempData

# Create your views here.

def home(request):
    return render(request,'SDhome.html',{'scholarships': tempData})