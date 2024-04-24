from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import HttpResponse
from SFWEScholarships.models import Application
from ScholarshipDonor.models import Scholarship
from Student.models import Student
from django.shortcuts import get_object_or_404
from Login.forms import CreateStudentForm
# Create your views here.

def home(request):
    currentUser = request.user #gets current logged in user
    #student = get_object_or_404(Student, student_info_id = currentUser.id)#filters the students by last name and first nam
    return render(request,'Shome.html', {'currentUser' : currentUser})

def ViewScholarships(request):
    scholarships_object = Scholarship.objects.all()
    context = {'scholarships_object' : scholarships_object}
    return render(request, 'SViewScholarships.html', context)

def ViewProfile(request):
    currentUser = request.user
    student = get_object_or_404(Student, student_info_id = currentUser.id)
    context = {'student' : student, 'currentUser' : currentUser}
    return render(request, 'SViewProfile.html', context)

def CheckAppStatus(request):
    currentUser = request.user
    student = get_object_or_404(Student, student_info_id = currentUser.id)
    application_object = Application.objects.all()
    context = {'application_object' : application_object, 'student' : student}
    return render(request, 'SCheckAppStatus.html', context)

def ViewScholarshipInfo(request, scholarship_id):
    scholarship = get_object_or_404(Scholarship, pk=scholarship_id) #scholarship is set to a object not a class
    return render(request, 'SViewScholarshipInfo.html', {'scholarship' : scholarship}) #this scholarship must be passed into the page other wise the page will break

def ViewCreateApplication(request, scholarship_id):
    currentUser = request.user #gets current logged in user
    student = get_object_or_404(Student, student_info_id = currentUser.id)#filters the students by last name and first name to find current user as a student object
    scholarship = get_object_or_404(Scholarship, pk=scholarship_id)
    return render(request, 'applicationForm.html', {'scholarship' : scholarship, 'student' : student, 'user' : currentUser}) #the one in quotes is what is called in html

def ViewEligableScholarships(request):
    currentUser = request.user
    student = get_object_or_404(Student, student_info_id = currentUser.id)
    scholarships_object = Scholarship.objects.all()
    context = {'scholarships_object' : scholarships_object, 'student' : student}
    return render(request, 'SViewEligableScholarships.html', context)


def editProfile(request):
    currentUser = request.user
    student = get_object_or_404(Student, student_info_id = currentUser.id)
    form = CreateStudentForm(request.POST, instance=student)
    if request.method == 'POST':
        if form.is_valid:
            form.save()
        else:
            form = CreateStudentForm()
        #context = {'form' : form}
    return render(request, 'SeditProfile.html',  {'form' : form})