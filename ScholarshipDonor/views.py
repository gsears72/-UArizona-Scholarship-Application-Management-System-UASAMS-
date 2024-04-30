from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.db import models
from django.http import JsonResponse
from ScholarshipAdministrator.forms import ScholarshipForm
from .models import Scholarship, Scholarship_change
from Login.models import User
from SFWEScholarships.models import Application

# Create your views here.

def home(request):
    scholarships = Scholarship.objects.all()
    return render(request,'SDhome.html',{'scholarships':scholarships})

def viewMore(request, scholarship_id):
    scholarship = get_object_or_404(Scholarship, pk = scholarship_id)
    form = ScholarshipForm(instance = scholarship) #this needs to be fixed but WHERE IS SCHOLARSHIP FORM??
    return render(request,'EditScholarshipView.html', {'scholarship':scholarship, 'form':form})

def ReviewApplication(request, application_id, scholarship_id):
    scholarship_object = Scholarship.objects.get(id=scholarship_id)
    application_object = Application.objects.get(pk=application_id)
    return render(request,'SDreviewApp.html', {'application_object': application_object, 'scholarship_object': scholarship_object})

def review_submit(request, application_id):
    application = Application.objects.get(pk=application_id)

    # Update the status of the application to 'reviewed'
    try:
        application.stauts = ('In Review')
        application.sr_status = request.POST.get('approval')
        application.score = request.POST.get('score')
        application.save()
        messages.success(request, "Application successfully updated")
        return redirect('ReviewApplicationSD', {})
    except:
        messages.success(request, "Application failed to update")
    return redirect('ReviewApplicationSD')

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

def createChangeRequest(request, scholarship_id):
    if request.method == "POST":
        scholarship_name = request.POST.get('scholarship_name')
        amount = request.POST.get('scholarship_amount')
        donor_name = request.POST.get('donor_full_name')
        donor_phone_number = request.POST.get('donor_phone_number')
        donor_email = request.POST.get('donor_email')
        total_avail = request.POST.get('num_scholarships_available')
        min_gpa = request.POST.get('required_gpa')
        major = request.POST.get('required_majors_or_minors')
        application_deadline = request.POST.get('application_deadline')
        other_requirements = request.POST.get('other_requirements')
        Scholarship_to_change = scholarship_id
        try:
            amount = float(amount)
            total_avail = float(total_avail)
            min_gpa = float(min_gpa)
        except ValueError:
            messages.error(request, "Please provide valid numerical values for amount, total available, and minimum GPA.")
            return redirect('EditScholarshipView')
        
        changeRequest = Scholarship_change(
            scholarship_name = scholarship_name,
            scholarship_amount = amount,
            donor_full_name = donor_name,
            donor_phone_number = donor_phone_number, # Assuming phone numbers as strings
            donor_email = donor_email,
            num_scholarships_available = total_avail,
            required_majors_or_minors = major,
            required_gpa = min_gpa,
            application_deadline = application_deadline,
            other_requirements = other_requirements,
            Scholarship_to_change = Scholarship_to_change,
        )
        changeRequest.save()

        messages.success(request, "Change request created successfully, Admin notified!")
        return redirect('SDhome') 
    else:
        return redirect('SDhome') 
  
  