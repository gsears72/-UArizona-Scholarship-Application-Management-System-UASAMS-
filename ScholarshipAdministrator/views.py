from django.shortcuts import render, redirect, get_list_or_404, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import HttpResponse
from django.core.mail import send_mail
import ScholarshipDonor
from ScholarshipDonor.models import Scholarship, Donor
from .forms import ScholarshipForm
from ScholarshipDonor.models import Scholarship_change
from SFWEScholarships.models import Application
from Login.models import User
from Student.models import Student
from EventLog.models import AvailableScholarshipsReport
from EventLog.models import ArchivedScholarshipsReport
from EventLog.models import AwardedScholarshipReport
from NotificationSystem.views import send_notification_S_DECISION, send_notification_SD_AWARDER
from NotificationSystem.models import Notification
from Login.models import User
#from ScholarshipAdministrator.forms import ScholarshipForm

# Create your views here.

def home(request):
    currentUser = request.user 
    notifications = Notification.objects.filter(recipient=request.user.pk)
    return render(request,'SAhome.html', {'currentUser': currentUser, 'notifications': notifications})

def create_scholarship(request):
    if request.method == 'POST':
            form = ScholarshipForm(request.POST)
            if form.is_valid():
                form.save()
                AvailableScholarshipsReport.objects.create(
                    Scholarship_name = form.cleaned_data['scholarship_name'],
                    Scholarship_Amount = form.cleaned_data['scholarship_amount'],
                    Scholarship_Donor_name = form.cleaned_data['donor_full_name'],
                    Scholarship_Donor_email = form.cleaned_data['donor_email'],
                    Scholarship_Donor_phone = form.cleaned_data['donor_phone_number'],
                    Scholarships_Avaliable = form.cleaned_data['num_scholarships_available'],
                    Scholarships_Majors_Minors = form.cleaned_data['required_majors_or_minors'],
                    Scholarships_GPA = form.cleaned_data['required_gpa'],
                    Scholarships_Deadline = form.cleaned_data['application_deadline'],
                    Scholarships_Description = form.cleaned_data['other_requirements']
                )
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
    Log_available = AvailableScholarshipsReport.objects.get(Scholarship_name=scholarship_name)
    if request.method == 'POST':
        form = ScholarshipForm(request.POST, instance=scholarship)
        if form.is_valid():
            form.save()
            
            Log_available.Scholarship_name = form.cleaned_data['scholarship_name']
            Log_available.Scholarship_Amount = form.cleaned_data['scholarship_amount']
            Log_available.Scholarship_Donor_name = form.cleaned_data['donor_full_name']
            Log_available.Scholarship_Donor_email = form.cleaned_data['donor_email']
            Log_available.Scholarship_Donor_phone = form.cleaned_data['donor_phone_number']
            Log_available.Scholarships_Avaliable = form.cleaned_data['num_scholarships_available']
            Log_available.Scholarships_Majors_Minors = form.cleaned_data['required_majors_or_minors']
            Log_available.Scholarships_GPA = form.cleaned_data['required_gpa']
            Log_available.Scholarships_Deadline = form.cleaned_data['application_deadline']
            Log_available.Scholarships_Description = form.cleaned_data['other_requirements']
            Log_available.save()
            return redirect('scholarship_list')
    else:
        form = ScholarshipForm(instance=scholarship)
    return render(request, 'SAeditscholarship.html', {'form': form})

def delete_scholarship_page(request, scholarship_name):
    scholarship = Scholarship.objects.get(scholarship_name=scholarship_name)
    return render(request, 'SAdeletescholarship.html', {'scholarship': scholarship})

def delete_scholarship_db(request, scholarship_name):
    scholarship = Scholarship.objects.get(scholarship_name=scholarship_name)
    ArchivedScholarshipsReport.objects.create(
        Scholarship_name = scholarship.scholarship_name,
        Scholarship_Amount = scholarship.scholarship_amount,
        Scholarship_Donor_name = scholarship.donor_full_name,
        Scholarship_Donor_email = scholarship.donor_email,
        Scholarship_Donor_phone = scholarship.donor_phone_number,
        Scholarships_Avaliable = scholarship.num_scholarships_available,
        Scholarships_Majors_Minors = scholarship.required_majors_or_minors,
        Scholarships_GPA = scholarship.required_gpa,
        Scholarships_Deadline = scholarship.application_deadline,
        Scholarships_Description = scholarship.other_requirements
    )
    AvailableScholarshipsReport.objects.get(Scholarship_name=scholarship_name).delete()
    scholarship.delete()
    return render(request, 'SAscholarshipdeleted.html', {})

def viewChangeRequest(request):
    changeRequests = Scholarship_change.objects.all()
    return render(request, 'viewChangeRequest.html', {'changeRequests': changeRequests})

def denyChangeRequest(request, change_id):
    changeRequest = get_object_or_404(Scholarship_change, pk=change_id)
    if request.method == "POST":
        changeRequest.delete()
        messages.success(request, "Change request denied.")
        return redirect('viewChangeRequest')
    
def approveChangeRequest(request, change_id):
    changeRequest = get_object_or_404(Scholarship_change, pk=change_id)
    scholarship = get_object_or_404(Scholarship, pk=changeRequest.Scholarship_to_change)
    Log_available = AvailableScholarshipsReport.objects.get(Scholarship_name=scholarship_name)
    if request.method == "POST":
        scholarship.scholarship_name = changeRequest.scholarship_name
        scholarship.scholarship_amount = changeRequest.scholarship_amount
        scholarship.donor_full_name = changeRequest.donor_full_name
        scholarship.donor_email = changeRequest.donor_email
        scholarship.donor_phone_number = changeRequest.donor_phone_number
        scholarship.num_scholarships_available = changeRequest.num_scholarships_available
        scholarship.required_gpa = changeRequest.required_gpa
        scholarship.application_deadline = changeRequest.application_deadline
        scholarship.required_majors_or_minors = changeRequest.required_majors_or_minors 
        scholarship.other_requirements = changeRequest.other_requirements
        scholarship.save()

        Log_available.Scholarship_name = changeRequest.scholarship_name
        Log_available.Scholarship_Amount = changeRequest.scholarship_amount
        Log_available.Scholarship_Donor_name = changeRequest.donor_full_name
        Log_available.Scholarship_Donor_email = changeRequest.donor_email
        Log_available.Scholarship_Donor_phone = changeRequest.donor_phone_number
        Log_available.Scholarships_Avaliable = changeRequest.num_scholarships_available
        Log_available.Scholarships_Majors_Minors = changeRequest.required_majors_or_minors
        Log_available.Scholarships_GPA = changeRequest.required_gpa
        Log_available.Scholarships_Deadline = changeRequest.application_deadline
        Log_available.Scholarships_Description = changeRequest.other_requirements
        Log_available.save()

        changeRequest.delete()
        messages.success(request, "Change request approved.")
        return redirect('viewChangeRequest')

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
    
def review_scholarship_list(request):
    applications_object = Application.objects.filter(
        stauts='In Review'
        )
    return render(request, 'ViewScholarshipsAR.html', {'applications_object': applications_object})

def application_listy(request, scholarship_id):
    scholarship = get_object_or_404(Scholarship, id=scholarship_id)
    query = request.GET.get('q', '')  # Get the search query from 'q' parameter, default to empty string
    
    applications = Application.objects.filter(scholarship_id=scholarship_id)
    
    if query:
        # Filter applications based on the student's first name
        applications = applications.filter(student__student_info__First_name__icontains=query)
    
    return render(request, "SAapplicationlist.html", {
        'applications': applications,
        'scholarship': scholarship,
    })

def review_application(request, application_id, scholarship_id):
    application_object = Application.objects.get(pk=application_id)
    scholarship_object = Scholarship.objects.get(id=scholarship_id)
    return render(request, "SAReviewApplication.html", {
        'application_object': application_object,
        'scholarship_object': scholarship_object
    })

def application_approval(request, application_id, scholarship_id):
    scholarship_object = Scholarship.objects.get(id=scholarship_id)
    application_object = Application.objects.get(pk=application_id)
    # Update the status of the application to 'reviewed'
    application_object.stauts = request.POST.get('approval')
    application_object.save()
    messages.success(request, "Application status updated.")

    # Event Log
    AwardedScholarshipReport.objects.create(
        Scholarship_Name = scholarship_object.scholarship_name,
        Scholarship_Amount = scholarship_object.scholarship_amount,
        Student_Awarded_Name = application_object.student.student_info.First_name+" "+application_object.student.student_info.Last_name,
        Student_Awarded_NetID = application_object.student.student_info.Net_ID,
        Student_Awarded_Email = application_object.student.student_info.email,
        Student_Awarded_Major = application_object.student.major,
        Student_Awarded_GPA = application_object.student.gpa,
        Student_Awarded_Ethnicity = application_object.student.ethnicity,
        
    )


    if (application_object.stauts == "Approved"):
        donor = User.objects.filter(email = scholarship_object.donor_email)
        print(donor)
        Student_name = application_object.student.student_info.First_name+" "+application_object.student.student_info.Last_name
        send_notification_S_DECISION(application_object.student.student_info, "ACCEPTED", scholarship_object.scholarship_name)

        #Can Be Uncommented Once Database has correctly mapped data
        # send_notification_SD_AWARDER(donor, scholarship_object.scholarship_name,Student_name)
    else:
        send_notification_S_DECISION(application_object.student.student_info, "REJECTED", scholarship_object.scholarship_name)


    return render(request, "SAhome.html", {
        'applications': application_object,
        'scholarship_object': scholarship_object
    })

def Reports(request):
    return render(request, 'SAreports.html', {})