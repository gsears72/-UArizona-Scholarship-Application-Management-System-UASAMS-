from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    class Role(models.TextChoices):
        Student = 'Student', 'Student'
        ScholarshipAdministrator = 'Scholarship Administrator','Scholarship Administrator'
        ApplicantReviewer = 'Applicant Reviewer', 'Applicant Reviewer'
        ScholarshipProvider = 'Scholarship Provider', 'Scholarship Provider'
        ScholarshipFundSteward = 'Scholarship Fund Steward ', 'Scholarship Fund Steward'
        AuthorizedENGRStaff = 'Authorized ENGR Staff', 'Authorized ENGR Staff'
        ENGRITSupportStaff = 'ENGR IT Support Staff', 'ENGR IT Support Staff'

    base_role = Role.ENGRITSupportStaff

    role = models.CharField(max_length=50, choices=Role.choices, default=Role.ENGRITSupportStaff)

    def save(self,*args, **kwargs):
        if not self.pk:
            self.role = self.base_role
            return super().save(*args, **kwargs)
        

class Student(User):

    base_role = User.Role.Student

    class Meta:
        proxy = True

class ScholarshipAdministrator(User):

    base_role = User.Role.ScholarshipAdministrator

    class Meta:
        proxy = True

class ApplicantReviewer(User):

    base_role = User.Role.ApplicantReviewer

    class Meta:
        proxy = True

class ScholarshipProvider(User):

    base_role = User.Role.ScholarshipProvider

    class Meta:
        proxy = True

class ScholarshipFundSteward(User):

    base_role = User.Role.ScholarshipFundSteward

    class Meta:
        proxy = True


class AuthorizedENGRStaffent(User):

    base_role = User.Role.AuthorizedENGRStaff

    class Meta:
        proxy = True







