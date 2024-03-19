from django.db import models

# Create your models here.
class applicantReviewer(models.Model):
    applicantReviewer_info = models.OneToOneField('Login.User', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.username}"
