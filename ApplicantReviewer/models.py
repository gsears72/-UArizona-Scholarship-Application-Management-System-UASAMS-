from django.db import models

# Create your models here.
class applicantReviewer(models.Model):
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

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.username}"
    

