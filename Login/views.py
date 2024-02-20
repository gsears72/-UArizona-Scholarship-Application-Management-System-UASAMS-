from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


from .forms import CreateStudentForm

# Create your views here.
def login_user(request):
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
    messages.success(request,'You Were Logged Out')
    logout(request)
    return redirect('home')


def studentRegister(request):
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
    if request.method == 'POST':
        pass
    else:
        return redirect('login')
    
def scholorshipdonorregisterRegister(request):
    if request.method == 'POST':
        pass
    else:
        return redirect('login')
    
def applicantreviewerRegister(request):
    if request.method == 'POST':
        pass
    else:
        return redirect('login')
    


