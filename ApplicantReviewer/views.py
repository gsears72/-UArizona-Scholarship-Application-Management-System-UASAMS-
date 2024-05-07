from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import get_list_or_404
from django.shortcuts import get_object_or_404
from django.core.mail import send_mail

from NotificationSystem.views import send_notification_S_DECISION, send_notification_SA_REVIWFINISHED
from ScholarshipDonor.models import Scholarship
from SFWEScholarships.models import Application
from Student.models import Student
from Login.models import User
from Login.models import ScholarshipAdministrator
from NotificationSystem.models import Notification
from Login.models import User

def ARhome(request):
    if User.is_authenticated:
        notifications = Notification.objects.filter(recipient=request.user.pk)
    else:
        notifications = None
    return render(request,'ARhome.html',{})

def ARreports(request):
    return render(request, 'ARreports.html', {})

def ViewScholarshipsAR(request):
    scholarships_object = Scholarship.objects.all()
    context = {'scholarships_object' : scholarships_object}
    return render(request,'ViewScholarshipsAR.html', context)

def SearchApplicants(request):
    applications = Application.objects.all()
    return render(request,'SearchApplicants.html',{'applications': applications})

def MyReviewedApps(request):
    application_object = Application.objects.all()
    return render(request,'MyReviewedApps.html',{'application_object': application_object})

def ReviewConfirmation(request):
    return render(request,'ReviewConfirmation.html', {})


def ARApproved(request):
    application_object = Application.objects.all()
    return render(request,'ARApproved.html', {'application_object':application_object})

def ViewApplicants(request, scholarship_id):
    user_object = User.objects.all()
    scholarship = scholarship_id
    scholarship_object = Scholarship.objects.get(id = scholarship_id)
    application_object = Application.objects.all()
    return render(request,'ViewApplicants.html',{'user_object': user_object, 'scholarship_object': scholarship_object, 'application_object': application_object, 'scholarship_id': scholarship})

def ViewEligibleApplicants(request, scholarship_id):
    scholarship = scholarship_id
    scholarship_object = Scholarship.objects.get(id = scholarship_id)
    application_object = Application.objects.all()
    return render(request,'ViewEligibleApplicants.html',{'scholarship_object': scholarship_object, 'application_object': application_object, 'scholarship_id': scholarship})

def ReviewApplication(request, application_id, scholarship_id):
    scholarship_object = Scholarship.objects.get(id=scholarship_id)
    application_object = Application.objects.get(pk=application_id)
    return render(request,'ReviewApplication.html',{'application_object': application_object, 'scholarship_object': scholarship_object})

def application_list(request):
    query = request.GET.get('q', '')  # Get the search query from 'q' parameter, default to empty string
    if query:
        # Filter scholarships based on the search query
        user = User.objects.get(First_name__icontains=query)
        print(user.First_name)
        curr_student = Student.objects.get(student_info=user)
        print(curr_student.major)
        applications = Application.objects.filter(
            student=curr_student
            # You can add more fields to filter upon as needed, like donor_name__icontains=query, etc.
        )
    else:
        applications = Application.objects.all()
    return render(request, 'SearchApplicants.html', {'applications': applications})


def scholarship_list_AR(request):
    query = request.GET.get('q', '')  # Get the search query from 'q' parameter, default to empty string
    if query:
        # Filter scholarships based on the search query
        scholarships_object = Scholarship.objects.filter(
            scholarship_name__icontains=query
            # You can add more fields to filter upon as needed, like donor_name__icontains=query, etc.
        )
    else:
        scholarships_object = None
    
    return render(request, 'ViewScholarshipsAR.html', {'scholarships_object': scholarships_object})

def review_submitAR(request, application_id):
    application = Application.objects.get(pk=application_id)
    # Update the status of the application to 'reviewed'
    application.stauts = ('In Review')
    application.sr_status = request.POST.get('approval')
    application.score = request.POST.get('score')

    application.save()

    # Send notification to Admins
    admin_user = User.objects.filter(role='Scholarship Administrator')
    for admin in admin_user:
        send_notification_SA_REVIWFINISHED(admin, application.scholarship.scholarship_name)
        
    return redirect("ViewScholarshipsAR")