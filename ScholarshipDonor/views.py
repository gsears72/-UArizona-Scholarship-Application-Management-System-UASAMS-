from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.db import models
from django.http import JsonResponse
from ScholarshipAdministrator.forms import ScholarshipForm
from .models import Scholarship
from Login.models import User
from SFWEScholarships.models import Application
from ScholarshipDonor.models import Donor

# Create your views here.

def home(request):
    scholarships = Scholarship.objects.all()
    currentUser = request.user
    donor = get_object_or_404(Donor, donor_info_id = currentUser.id)
    context = {'scholarships' : scholarships, 'donor' : donor, 'currentUser' : currentUser}
    return render(request,'SDhome.html',context)
    return render(request,'SDhome.html',{'scholarships':scholarships})

def viewMore(request, scholarship_id):
    scholarship = get_object_or_404(Scholarship, pk = scholarship_id)
    form = ScholarshipForm(instance = scholarship) #this needs to be fixed but WHERE IS SCHOLARSHIP FORM??
    return render(request,'EditScholarshipView.html', {'scholarship':scholarship, 'form':form})

def ViewApplicantsSD(request, scholarship_id):
    user_object = User.objects.all()
    scholarship = scholarship_id
    scholarship_object = Scholarship.objects.get(id = scholarship_id)
    application_object = Application.objects.all()
    return render(request,'ViewApplicantsSD.html',{'user_object': user_object, 'scholarship_object': scholarship_object, 'application_object': application_object, 'scholarship_id': scholarship})

def ViewEligibleApplicantsSD(request, scholarship_id):
    scholarship = scholarship_id
    scholarship_object = Scholarship.objects.get(id = scholarship_id)
    application_object = Application.objects.all()
    return render(request,'ViewEligibleApplicantsSD.html',{'scholarship_object': scholarship_object, 'application_object': application_object, 'scholarship_id': scholarship})


