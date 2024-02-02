from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.
def login_user(request):
    if request.method == 'POST':
        username = request.POST["Username"]
        password = request.POST["Password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request,'success')
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
