from django.db import models
from ScholarshipDonor.models import Scholarship
from Student.models import Student

# Create your models here.
class Application(models.Model):
    STATUS = (
        ('Submitted', 'Submitted'), 
        ('In Reivew', 'In Review'), 
        ('Approved', 'Approved'), 
        ('Rejected', 'Rejected')
    )
    
    SR_STATUS = (
        ('In Reivew', 'In Review'),
        ('Approved', 'Approved'), 
        ('Rejected', 'Rejected')
    )
    
    
    

    scholarship = models.ForeignKey(Scholarship, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    stauts = models.CharField(max_length = 20, choices = STATUS, default = 'Submitted')
    personal_statement = models.TextField()
    sr_status = models.CharField(max_length = 20, choices = SR_STATUS, default = 'In Review')
    score = models.IntegerField(max_length = 3, default = 0)
    resume = models.FileField(upload_to='resumes/',default='resumes/default.pdf')
    
    