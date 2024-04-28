from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import FileResponse, HttpResponse, HttpResponseRedirect
from SFWEScholarships.models import Application, Document
from ScholarshipDonor.models import Scholarship
from Student.models import Student
from django.shortcuts import get_object_or_404
from SFWEScholarships.forms import ApplicationForm
from .forms import UploadFileForm
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
    application_object = Application.objects.all()
    context = {'application_object' : application_object}
    return render(request, 'SCheckAppStatus.html', context)

def openResume(request, application_id):
    application = get_object_or_404(Application, pk=application_id)
    filePath = application.resume.path
    return FileResponse(open(filePath, 'rb'))
def ViewScholarshipInfo(request, scholarship_id):
    scholarship = get_object_or_404(Scholarship, pk=scholarship_id) #scholarship is set to a object not a class
    return render(request, 'SViewScholarshipInfo.html', {'scholarship' : scholarship}) #this scholarship must be passed into the page other wise the page will break

def ViewApplication(request, scholarship_id):
    currentUser = request.user #gets current logged in user
    student = get_object_or_404(Student, student_info_id = currentUser.id)#filters the students by last name and first name to find current user as a student object
    scholarship = get_object_or_404(Scholarship, pk=scholarship_id)
    form = ApplicationForm()
    fileForm = UploadFileForm()
    return render(request, 'applicationForm.html', {'fileForm':fileForm, 'form':form, 'scholarship' : scholarship, 'student' : student, 'user' : currentUser}) #the one in quotes is what is called in html

def ViewEligableScholarships(request):
    currentUser = request.user
    student = get_object_or_404(Student, student_info_id = currentUser.id)
    scholarships_object = Scholarship.objects.all()
    context = {'scholarships_object' : scholarships_object, 'student' : student}
    return render(request, 'SViewEligableScholarships.html', context)


def createApplication(request, scholarship_id):
    if request.method == 'POST':
        personal_statement = request.POST.get('personal_statement')
        currentUser = request.user #gets current logged in user
        student = get_object_or_404(Student, student_info_id = currentUser.id)
        scholarship = get_object_or_404(Scholarship, pk=scholarship_id)
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():

            application = Application(
                student = student,
                scholarship = scholarship,
                personal_statement = personal_statement,
                resume = form.fields['resume'],
            )

            application.save()
            messages.success(request, "Application created successfully.")
        else:
            messages.success(request, "Application failed to upload resume.")
        return render(request, 'SViewScholarships.html', {})
    else:
        return render(request, 'SViewScholarships.html', {})