from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


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
            return redirect('home')
            # Redirect to a success page.
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
    return redirect('home')



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
             raw_password = form.cleaned_data.get('password')
             user = authenticate(email=email, password=raw_password)
             login(request, user)
             messages.success(request,'Account Created') 
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
             raw_password = form.cleaned_data.get('password')
             user = authenticate(email=email, password=raw_password)
             login(request, user)
             messages.success(request,'Account Created') 
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
             raw_password = form.cleaned_data.get('password')
             user = authenticate(email=email, password=raw_password)
             login(request, user)
             messages.success(request,'Account Created') 
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
             raw_password = form.cleaned_data.get('password')
             user = authenticate(email=email, password=raw_password)
             login(request, user)
             messages.success(request,'Account Created') 
             return redirect("home")
         else:
                context = {'form': form}
                return render(request,'authenticate/applicant_reviewer_register.html',context)
    else:
        form = CreateApplicantReviewerForm()
        context = {'form': form}
        return render(request,'authenticate/scholarship_donor_register.html',context)
    


