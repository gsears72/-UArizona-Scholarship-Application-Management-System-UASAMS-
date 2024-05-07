from django.shortcuts import render
from .models import AvailableScholarshipsReport, ArchivedScholarshipsReport, ScholarshipApplicationReport, AwardedScholarshipReport, StudentDemographicsReport, ActiveDonorsReport
import csv
from django.http import HttpResponse

# Create your views here.

def generate_AvailableScholarshipsReport(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="AvailableScholarshipsReport.csv"'

    writer = csv.writer(response)
    for item in AvailableScholarshipsReport.objects.all():
        writer.writerow([item.Scholarship_name, item.Scholarship_Amount, item.Scholarship_Donor_name, item.Scholarship_Donor_email, item.Scholarship_Donor_phone, item.Scholarships_Avaliable, item.Scholarships_Majors_Minors, item.Scholarships_GPA, item.Scholarships_Deadline, item.Scholarships_Description])

    return response

def generate_ArchivedScholarshipsReport(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="ArchivedScholarshipsReport.csv"'

    writer = csv.writer(response)
    for item in ArchivedScholarshipsReport.objects.all():
        writer.writerow([item.Scholarship_name, item.Scholarship_Amount, item.Scholarship_Donor_name, item.Scholarship_Donor_email, item.Scholarship_Donor_phone, item.Scholarships_Avaliable, item.Scholarships_Majors_Minors, item.Scholarships_GPA, item.Scholarships_Deadline, item.Scholarships_Description])

    return response

def generate_ScholarshipApplicationReport(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="ScholarshipApplicationReport.csv"'

    writer = csv.writer(response)
    for item in ScholarshipApplicationReport.objects.all():
        writer.writerow([item.Scholarship_Name, item.Applicant_Name, item.Applicant_Pronouns, item.Applicant_NetID, item.Applicant_Major, item.Applicant_GPA, item.Applicant_Year, item.Applicant_Ethnicity, item.Applicant_Personal_Statement])

    return response

def generate_AwardedScholarshipReport(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="AwardedScholarshipReport.csv"'

    writer = csv.writer(response)
    for item in AwardedScholarshipReport.objects.all():
        writer.writerow([item.Scholarship_Name, item.Scholarship_Amount, item.Student_Awarded_Name, item.Student_Awarded_NetID, item.Student_Awarded_Major, item.Student_Awarded_GPA, item.Student_Awarded_Ethnicity, item.Student_Awarded_Email])\
        
    return response

def generate_StudentDemographicsReport(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="StudentDemographicsReport.csv"'

    writer = csv.writer(response)
    for item in StudentDemographicsReport.objects.all():
        writer.writerow([item.Student_Name, item.Student_Pronouns, item.Student_NetID, item.Student_Major, item.Student_GPA, item.Student_Year, item.Student_Ethnicity, item.Student_Personal_Statement])

    return response

def generate_ActiveDonorsReport(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="ActiveDonorsReport.csv"'

    writer = csv.writer(response)
    for item in ActiveDonorsReport.objects.all():
        writer.writerow([item.Donor_Name, item.Donor_Phone, item.Donor_Email, item.Donor_Amount, item.Donor_Scholarships])

    return response


