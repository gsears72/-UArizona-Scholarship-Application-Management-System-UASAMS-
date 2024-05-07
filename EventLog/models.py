from django.db import models

# Create your models here.

class AvailableScholarshipsReport(models.Model):

    Scholarship_name = models.CharField(max_length=50)
    Scholarship_Amount = models.IntegerField()
    Scholarship_Donor_name = models.CharField(max_length=50)
    Scholarship_Donor_email = models.EmailField()
    Scholarship_Donor_phone = models.CharField(max_length=15)
    Scholarships_Avaliable = models.IntegerField()
    Scholarships_Majors_Minors = models.CharField(max_length=50)
    Scholarships_GPA = models.FloatField()
    Scholarships_Deadline = models.DateField()
    Scholarships_Description = models.TextField()

class ArchivedScholarshipsReport(models.Model):

    Scholarship_name = models.CharField(max_length=50)
    Scholarship_Amount = models.IntegerField()
    Scholarship_Donor_name = models.CharField(max_length=50)
    Scholarship_Donor_email = models.EmailField()
    Scholarship_Donor_phone = models.CharField(max_length=15)
    Scholarships_Avaliable = models.IntegerField()
    Scholarships_Majors_Minors = models.CharField(max_length=50)
    Scholarships_GPA = models.FloatField()
    Scholarships_Deadline = models.DateField()
    Scholarships_Description = models.TextField()


class ScholarshipApplicationReport(models.Model):
    
    Scholarship_Name = models.CharField(max_length=50)
    Applicant_Name = models.CharField(max_length=50)
    Applicant_Pronouns = models.CharField(max_length=50)
    Applicant_NetID = models.CharField(max_length=50)
    Applicant_Major = models.CharField(max_length=50)
    Applicant_GPA = models.FloatField()
    Applicant_Year = models.CharField(max_length=50)
    Applicant_Ethnicity = models.CharField(max_length=50)
    Applicant_Personal_Statement = models.TextField()

class AwardedScholarshipReport(models.Model):
    
    Scholarship_Name = models.CharField(max_length=50)
    Scholarship_Amount = models.IntegerField()
    Student_Awarded_Name = models.CharField(max_length=50)
    Student_Awarded_NetID = models.CharField(max_length=50)
    Student_Awarded_Major = models.CharField(max_length=50)
    Student_Awarded_GPA = models.FloatField()
    Student_Awarded_Ethnicity = models.CharField(max_length=50)
    Student_Awarded_Email = models.EmailField()

class StudentDemographicsReport(models.Model):

    Student_Name = models.CharField(max_length=50)
    Student_Pronouns = models.CharField(max_length=50)
    Student_NetID = models.CharField(max_length=50)
    Student_Major = models.CharField(max_length=50)
    Student_GPA = models.FloatField()
    Student_Year = models.CharField(max_length=50)
    Student_Ethnicity = models.CharField(max_length=50)
    Student_Personal_Statement = models.TextField()


class ActiveDonorsReport(models.Model):
    
    Donor_Name = models.CharField(max_length=50)
    Donor_Email = models.EmailField()
    Donor_Phone = models.CharField(max_length=15)
    Donor_Amount = models.IntegerField()
    Donor_Scholarships = models.IntegerField()

    
