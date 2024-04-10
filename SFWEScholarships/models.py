from django.db import models
from ScholarshipDonor.models import Scholarship
from Student.models import Student


# Create your models here.
class Application(models.Model):
    STATUS = (
        ('Submitted', 'Submitted'), 
        ('In Review', 'In Review'), 
        ('Approved', 'Approved'), 
        ('Rejected', 'Rejected')
    )

    scholarship = models.ForeignKey(Scholarship, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    stauts = models.CharField(max_length = 20, choices = STATUS, default = 'Submitted')
    personal_statement = models.TextField(max_length = 1000)
    score = models.IntegerField(default = 0)
    sr_status = models.CharField(max_length = 20, choices = STATUS, default = 'In Review')

    # def __str__(self):
    #     return f"Application for {self.scholarship.scholarship_name} by "