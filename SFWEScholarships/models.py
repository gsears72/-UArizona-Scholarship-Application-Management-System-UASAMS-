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


    scholarship = models.ForeignKey(Scholarship, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    status = models.CharField(max_length = 20, choices = STATUS, default = 'Submitted')
    essay = models.TextField()

    def __str__(self):
        return f"Application for {self.scholarship.scholarship_name} by {self.student.username}"