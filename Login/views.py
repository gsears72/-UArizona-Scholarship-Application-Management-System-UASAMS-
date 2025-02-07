from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from Student.models import Student
from ScholarshipAdministrator.models import scholarshipAdministrator
from ScholarshipDonor.models import Donor
from ApplicantReviewer.models import applicantReviewer
from EventLog.models import StudentDemographicsReport
from EventLog.models import ActiveDonorsReport


from .forms import CreateStudentForm, CreateScholorshipAdministratorForm, CreateScholorshipDonorForm, CreateApplicantReviewerForm

# Create your views here.
def login_user(request):
    """
    Logs in a user.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The HTTP response object.

    """
    if request.method == 'POST':
        email = request.POST["Email"]
        password = request.POST["Password"]
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            messages.success(request,'Login Sucessful')
            match user.role:
                case 'Scholarship Donor':
                    return redirect('SDhome')
                case 'Scholarship Administrator':
                    return redirect('SAhome')
                case 'Applicant Reviewer':   
                    return redirect('ARhome')   
                case 'Student':
                    return redirect('Shome')
        else:
            messages.success(request,'There Was An Error Logging In, Please Try Again')
            return redirect('login')

    else:
        return render(request, 'authenticate/login.html',{})



def logout_user(request):
    """
    Logs out the user and redirects to the home page.

    Parameters:
    - request: The HTTP request object.

    Returns:
    - A redirect response to the home page.
    """
    messages.success(request,'You Were Logged Out')
    logout(request)
    return redirect('login')



def studentRegister(request):
    """
    View function for student registration.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The HTTP response object.

    """
    form = CreateStudentForm()
    if request.method == 'POST':
        form = CreateStudentForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(email=email, password=raw_password)
            login(request, user)
            messages.success(request,'Account Created')
            Student.objects.create(student_info=user,
                                    preferred_pronoun = form.cleaned_data.get('Preferred_Pronoun'),
                                    major = form.cleaned_data.get('Major'),
                                    minor = form.cleaned_data.get('Minor'),
                                    gpa = form.cleaned_data.get('GPA'),
                                    current_year = form.cleaned_data.get('Current_Year'), 
                                    ethnicity = form.cleaned_data.get('Ethnicity'),
                                    personal_statement_essay = form.cleaned_data.get('Personal_Statement'),
                                    work_experience = form.cleaned_data.get('Work_Experience'))
            StudentDemographicsReport.objects.create(
            Student_Name = form.cleaned_data.get('First_name') + ' ' + form.cleaned_data.get('Last_name'),
            Student_Pronouns = form.cleaned_data.get('Preferred_Pronoun'),
            Student_NetID = form.cleaned_data.get('Net_ID'),
            Student_Major = form.cleaned_data.get('Major'),             Student_GPA = form.cleaned_data.get('GPA'),
            Student_Year = form.cleaned_data.get('Current_Year'),
            Student_Ethnicity = form.cleaned_data.get('Ethnicity'),
            Student_Personal_Statement = form.cleaned_data.get('Personal_Statement')
            )


            return redirect("home")
        else:
                context = {'form': form}
                return render(request,'authenticate/student_register.html',context)
    else:
        form = CreateStudentForm()
        context = {'form': form}
        return render(request,'authenticate/student_register.html',context)



def scholorshipadminstratoRegister(request):
    """
    View function for registering a scholarship administrator.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The HTTP response object.

    """
    form = CreateScholorshipAdministratorForm()
    if request.method == 'POST':
        form = CreateScholorshipAdministratorForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(email=email, password=raw_password)
            login(request, user)
            messages.success(request,'Account Created')
            scholarshipAdministrator.objects.create(scholarshipAdministrator_info=user) 
            return redirect("home")
        else:
                context = {'form': form}
                return render(request,'authenticate/scholarship_administrator_register.html',context)
    else:
        form = CreateScholorshipAdministratorForm()
        context = {'form': form}
        return render(request,'authenticate/scholarship_administrator_register.html',context)




def scholorshipdonorregisterRegister(request):
    """
    Register a scholarship donor.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The HTTP response object.

    """
    form = CreateScholorshipDonorForm()
    if request.method == 'POST':
        form = CreateScholorshipDonorForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(email=email, password=raw_password)
            login(request, user)
            messages.success(request,'Account Created')
            Donor.objects.create(donor_info=user)
            ActiveDonorsReport.objects.create(
                Donor_Name = form.cleaned_data.get('First_name') + ' ' + form.cleaned_data.get('Last_name'),
                Donor_Email = form.cleaned_data.get('email'),
                Donor_Phone = form.cleaned_data.get('Phone_number'),
                Donor_Amount = 0,
                Donor_Scholarships =0,
            ) 
            return redirect("home")
        else:
                context = {'form': form}
                return render(request,'authenticate/scholarship_donor_register.html',context)
    else:
        form = CreateScholorshipDonorForm()
        context = {'form': form}
        return render(request,'authenticate/scholarship_donor_register.html',context)
    

    
    
def applicantreviewerRegister(request):
    """
    View function for registering an applicant reviewer.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The HTTP response object.

    """
    form = CreateApplicantReviewerForm()
    if request.method == 'POST':
        form = CreateApplicantReviewerForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(email=email, password=raw_password)
            login(request, user)
            messages.success(request,'Account Created')
            applicantReviewer.objects.create(applicantReviewer_info=user)

            return redirect("home")
        else:
            context = {'form': form}
            return render(request,'authenticate/applicant_reviewer_register.html',context)
    else:
        form = CreateApplicantReviewerForm()
        context = {'form': form}
        return render(request,'authenticate/applicant_reviewer_register.html',context)
    


