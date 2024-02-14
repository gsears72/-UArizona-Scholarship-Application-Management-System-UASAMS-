from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.db import models
from django.http import JsonResponse
from .tempData import tempData
from .models import Scholarship

# Create your views here.

def home(request):
    return render(request,'SDhome.html',{'scholarships': tempData})
