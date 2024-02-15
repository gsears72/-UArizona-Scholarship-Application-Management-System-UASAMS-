from django.db import models
from ScholarshipDonor.models import Scholarship
from Student.models import Student

# Create your models here.
class Application(models.Model):
    scholarship = models.ForeignKey(Scholarship, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)

    def __str__(self):
        return f"Application for {self.scholarship.scholarship_name} by {self.student.username}"