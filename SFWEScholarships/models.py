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
    
    SR_STATUS_CHOICES = (
        ('In Reivew', 'In Review'),
        ('Approved', 'Approved'), 
        ('Rejected', 'Rejected')
    )
    
    

    scholarship = models.ForeignKey(Scholarship, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    stauts = models.CharField(max_length = 20, choices = STATUS, default = 'Submitted')
    personal_statement = models.TextField()
    sr_status = models.CharField(max_length = 20, choices = SR_STATUS_CHOICES, default = 'In Review')
    score = models.IntegerField(validators=[MaxValueValidator(100)], default = 0)
    