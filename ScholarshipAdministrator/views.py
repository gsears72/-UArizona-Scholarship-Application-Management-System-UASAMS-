from django.shortcuts import render, redirect, get_list_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import HttpResponse
from ScholarshipDonor.models import Scholarship

# Create your views here.

def home(request):
    return render(request,'SAhome.html',{})

def create_scholarship(request):
    return render(request, 'SAcreatescholarship.html', {})

def scholarship_list(request):
    scholarships_list = Scholarship.objects.all()
    return render(request, 'SAscholarshiplist.html', {'scholarships': scholarships_list})

def edit_scholarship(request, scholarship_name):
    scholarship = Scholarship.objects.get(scholarship_name=scholarship_name)
    return render(request, 'SAeditscholarship.html', {'scholarship': scholarship})

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
