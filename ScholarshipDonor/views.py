from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.db import models
from django.http import JsonResponse
from ScholarshipAdministrator.forms import ScholarshipForm
from .models import Scholarship

# Create your views here.

def home(request):
    scholarships = Scholarship.objects.all()
    return render(request,'SDhome.html',{'scholarships':scholarships})

def viewMore(request, scholarship_id):
    scholarship = get_object_or_404(Scholarship, pk = scholarship_id)
    form = ScholarshipForm(instance = scholarship) #this needs to be fixed but WHERE IS SCHOLARSHIP FORM??
    return render(request,'EditScholarshipView.html', {'scholarship':scholarship, 'form':form})


