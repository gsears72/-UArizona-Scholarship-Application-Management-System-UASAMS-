from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import get_list_or_404
from django.shortcuts import get_object_or_404

from ScholarshipDonor.models import Scholarship
from SFWEScholarships.models import Application
from Student.models import Student

def ARhome(request):
    return render(request,'ARhome.html',{})

def ViewScholarshipsAR(request):
    scholarships_object = Scholarship.objects.all()
    context = {'scholarships_object' : scholarships_object}
    return render(request,'ViewScholarshipsAR.html', context)

def SearchApplicants(request):
    return render(request,'SearchApplicants.html',{})

def MyReviewedApps(request):
    application_object = Application.objects.all()
    return render(request,'MyReviewedApps.html',{})

def Approved(request):
    application_object = Application.objects.all()
    return render(request,'Approved.html',{})

def ViewApplicants(request, scholarship_id):
    scholarship = scholarship_id
    scholarship_object = Scholarship.objects.get(id = scholarship_id)
    application_object = Application.objects.all()
    return render(request,'ViewApplicants.html',{'scholarship_object': scholarship_object, 'application_object': application_object, 'scholarship_id': scholarship})

def ViewEligibleApplicants(request, scholarship_id):
    scholarship = scholarship_id
    scholarship_object = Scholarship.objects.get(id = scholarship_id)
    application_object = Application.objects.all()
    return render(request,'ViewEligibleApplicants.html',{'scholarship_object': scholarship_object, 'application_object': application_object, 'scholarship_id': scholarship})

def ReviewApplication(request, application_id, scholarship_id):
    scholarship_object = Scholarship.objects.get(id=scholarship_id)
    application_object = Application.objects.get(pk=application_id)
<<<<<<< HEAD
    return render(request,'ReviewAndScoring.html',{'application': application_object})
=======
    return render(request,'ReviewApplication.html',{'application_object': application_object, 'scholarship_object': scholarship_object})

def application_list(request):
    query = request.GET.get('q', '')  # Get the search query from 'q' parameter, default to empty string
    if query:
        # Filter scholarships based on the search query
        applications = Application.objects.filter(
            student__student_info__student_name__icontains=query
            # You can add more fields to filter upon as needed, like donor_name__icontains=query, etc.
        )
    else:
        applications = Scholarship.objects.all()
    
    return render(request, 'SearchApplicants.html', {'applications': applications})

def review_submit(request, application_id):
    application = get_object_or_404(Application, pk=application_id)
    
    # Update the status of the application to 'reviewed'
    application.stauts = 'In Review'
    application.save()
    
    return render(request, 'ReviewApplication.html', {'application': application})
>>>>>>> 40afdef28ebf60d831914b7e3f985d9233fa0007
