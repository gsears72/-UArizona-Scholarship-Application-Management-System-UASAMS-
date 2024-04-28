from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.db import models
from django.http import JsonResponse
from .models import Scholarship
from ScholarshipDonor.models import Donor

# Create your views here.

def home(request):
    scholarships = Scholarship.objects.all()
    currentUser = request.user
    donor = get_object_or_404(Donor, donor_info_id = currentUser.id)
    context = {'scholarships' : scholarships, 'donor' : donor, 'currentUser' : currentUser}
    return render(request,'SDhome.html',context)
