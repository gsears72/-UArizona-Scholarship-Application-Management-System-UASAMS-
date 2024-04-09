from django.db import models

# Create your models here.
class scholarshipAdministrator(models.Model):
    scholarshipAdministrator_info = models.OneToOneField('Login.User', on_delete=models.CASCADE, default = None)

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.username}"
