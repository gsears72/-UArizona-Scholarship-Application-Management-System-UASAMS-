from django.db import models

# Create your models here.
class Scholarship(models.Model):
    scholarship_name = models.CharField(max_length=100)
    scholarship_amount = models.DecimalField(max_digits=10, decimal_places=2)
    donor_full_name = models.CharField(max_length=100)
    donor_phone_number = models.CharField(max_length=15)  # Assuming phone numbers as strings
    donor_email = models.EmailField()
    num_scholarships_available = models.IntegerField()
    required_majors_or_minors = models.CharField(max_length=200)
    required_gpa = models.DecimalField(max_digits=3, decimal_places=2)
    application_deadline = models.DateField()
    other_requirements = models.TextField()

    def __str__(self):
        return self.scholarship_name

        
class Donor(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    security_question_1 = models.CharField(max_length=100)
    security_answer_1 = models.CharField(max_length=100)
    security_question_2 = models.CharField(max_length=100)
    security_answer_2 = models.CharField(max_length=100)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    net_id = models.CharField(max_length=50, blank=True, null=True)
    phone_number = models.CharField(max_length=15)  # Assuming phone numbers as strings
    email = models.EmailField()


        

    