from django.db import models

# Create your models here.  
class applicantReviewer(models.Model):
    # Basic Information
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)


