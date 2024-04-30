from django.shortcuts import render, redirect, get_list_or_404, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import HttpResponse
from django.core.mail import send_mail
from ScholarshipDonor.models import Scholarship
from .forms import ScholarshipForm
from SFWEScholarships.models import Application
from Login.models import User
from Student.models import Student
#from ScholarshipAdministrator.forms import ScholarshipForm

# Create your views here.

def home(request):
    return render(request,'SAhome.html',{})

def create_scholarship(request):
    if request.method == 'POST':
        form = ScholarshipForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('SAhome')  # Adjust the redirect to your needs
    else:
        form = ScholarshipForm()
    return render(request, 'SAcreatescholarship.html', {'form': form})

def scholarship_list(request):
    query = request.GET.get('q', '')  # Get the search query from 'q' parameter, default to empty string
    if query:
        # Filter scholarships based on the search query
        scholarships = Scholarship.objects.filter(
            scholarship_name__icontains=query
            # You can add more fields to filter upon as needed, like donor_name__icontains=query, etc.
        )
    else:
        scholarships = Scholarship.objects.all()
    
    return render(request, 'SAscholarshiplist.html', {'scholarships': scholarships})

def edit_scholarship(request, scholarship_name):
    scholarship = get_object_or_404(Scholarship, scholarship_name=scholarship_name)
    if request.method == 'POST':
        form = ScholarshipForm(request.POST, instance=scholarship)
        if form.is_valid():
            form.save()
            return redirect('scholarship_list')
    else:
        form = ScholarshipForm(instance=scholarship)
    return render(request, 'SAeditscholarship.html', {'form': form})

def delete_scholarship_page(request, scholarship_name):
    scholarship = Scholarship.objects.get(scholarship_name=scholarship_name)
    return render(request, 'SAdeletescholarship.html', {'scholarship': scholarship})

def delete_scholarship_db(request, scholarship_name):
    scholarship = Scholarship.objects.get(scholarship_name=scholarship_name)
    scholarship.delete()
    return render(request, 'SAscholarshipdeleted.html', {})



def create_scholarship_submit(request):
    if request.method == "POST":
        name = request.POST.get('name')
        amount = request.POST.get('amount')
        donor = request.POST.get('donor')
        total_avail = request.POST.get('totalAvail')
        min_gpa = request.POST.get('minGPA')
        major = request.POST.get('major')
        description = request.POST.get('description')
        
        if not name or not amount or not total_avail or not min_gpa:
            messages.error(request, "Please fill in all required fields.")
            return redirect('SAcreatescholarship') 
        try:
            amount = float(amount)
            total_avail = float(total_avail)
            min_gpa = float(min_gpa)
        except ValueError:
            messages.error(request, "Please provide valid numerical values for amount, total available, and minimum GPA.")
            return redirect('SAcreatescholarship')
        
        scholarship = Scholarship(
            name=name,
            amount=amount,
            donor=donor,
            totalAvail=total_avail,
            minGPA=min_gpa,
            major=major,
            dateCreated=None, 
            applicants=[], 
            awarded=[],
            description=description
        )
        scholarship.save()
        
        messages.success(request, "Scholarship created successfully.")
        return redirect('SAscholarshiplist') 
    else:
        return render(request, 'SAcreatescholarship.html')
    
def review_scholarship_list(request):
    applications_object = Application.objects.filter(
        stauts='In Review'
        )
    return render(request, 'ViewScholarshipsAR.html', {'applications_object': applications_object})

def application_list(request, scholarship_id):
    scholarship_object = Scholarship.objects.get(id=scholarship_id)
    query = request.GET.get('q', '')  # Get the search query from 'q' parameter, default to empty string
    if query:
        user = User.objects.get(First_name__icontains=query)
        curr_student = Student.objects.get(student_info=user)
        applications_object = Application.objects.filter(
            student=curr_student,
            scholarship__id=scholarship_id
        ) 
    else:
        # Retrieve all applications for the specified scholarship
        applications_object = Application.objects.filter(scholarship__id=scholarship_id)

    return render(request, "SAapplicationlist.html", {'applications_object': applications_object}, {'scholarship_object': scholarship_object})

def review_application(request, application_id, scholarship_id):
    application_object = Application.objects.get(pk=application_id)
    scholarship_object = Scholarship.objects.get(id=scholarship_id)
    return render(request, "SAreviewapplication.html", {'application_object': application_object}, {'scholarship_object': scholarship_object})

def application_approval(request, application_id, scholarship_id):
    scholarship_object = Scholarship.objects.get(id=scholarship_id)
    application_object = Application.objects.get(pk=application_id)
    # Update the status of the application to 'reviewed'
    application_object.stauts = ('approval')
    application_object.save()

    student_recipient_email = application_object.student.student_info.email
    student_subject = "Notification: Application Has Been " + application_object.stauts
    student_message = "Dear " + application_object.student.student_info.First_name + ", \n\tYour application for " + application_object.scholarship.scholarship_name + " has been " + application_object.stauts + ". For further information, please login to UASAMS."
    send_mail(student_subject, student_message, 'madrocarlson@gmail.com', student_recipient_email)
    return render(request, "SAapplicationlist.html", {'applications': application_object}, {'scholarship_object': scholarship_object})