from django.db import models

# Create your models here.  
class applicantReviewer(models.Model):
    # Basic Information
    applicantReviewer_info_id = models.OneToOneField('Login.User', on_delete=models.CASCADE, default = None)


