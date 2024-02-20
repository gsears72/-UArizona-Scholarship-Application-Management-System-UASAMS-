from django.utils import timezone
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.utils.translation import gettext_lazy as _

from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
import random
import string

class MyUserManager(BaseUserManager):

    def create_user(self, email, username, password=None, **extra_fields):
        if not email:
            raise ValueError("Users must have a email")
        if not username:
            raise ValueError("Users must have a username")
        
        
       
        user = self.model(email=self.normalize_email(email), username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, username, password, **extra_fields):
        user = self.create_user(
            email=self.normalize_email(email),
            username = username,
            password = password,
            **extra_fields
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True

        user.save(using=self._db)
        return user
    
    def create_student(self, email, username, password, **extra_fields):
        user = self.create_user(
            email=self.normalize_email(email),
            username = username,
            password = password,
            **extra_fields
        )
        user.role = 'Student'
        user.save(using=self._db)
        user.is_admin = False
        user.is_staff = False
        user.is_superuser = False
        return user
    
    def create_scholarship_administrator(self, email, username, password, **extra_fields):
        user = self.create_user(
            email=self.normalize_email(email),
            username = username,
            password = password,
            **extra_fields
        )
        user.role = 'Scholarship Administrator'
        user.save(using=self._db)
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = False
        return user
    
    def create_applicant_reviewer(self, email, username, password, **extra_fields):
        user = self.create_user(
            email=self.normalize_email(email),
            username = username,
            password = password,
            **extra_fields
        )
        user.role = 'Applicant Reviewer'
        user.save(using=self._db)
        user.is_admin = False
        user.is_staff = True
        user.is_superuser = False
        return user
    
    def create_scholarship_donor(self, email, username, password, **extra_fields):
        user = self.create_user(
            email=self.normalize_email(email),
            username = username,
            password = password,
            **extra_fields
        )
        user.role = 'Scholarship Donor'
        user.save(using=self._db)
        user.is_admin = False
        user.is_staff = False
        user.is_superuser = False
        return user
    
    def create_authorized_ENGR_staff(self, email, username, password, **extra_fields):
        user = self.create_user(
            email=self.normalize_email(email),
            username = username,
            password = password,
            **extra_fields
        )
        user.role = 'Authorized ENGR Staff'
        user.save(using=self._db)
        user.is_admin = False
        user.is_staff = True
        user.is_superuser = False
        return user
    
    def create_ENGR_IT_support_staff(self, email, username, password, **extra_fields):
        user = self.create_user(
            email=self.normalize_email(email),
            username = username,
            password = password,
            **extra_fields
        )
        user.role = 'ENGR IT Support Staff'
        user.save(using=self._db)
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        return user

def generate_random_email():
    domains = ["example.com", "test.com", "mydomain.com"]
    letters = string.ascii_lowercase
    email = ''.join(random.choice(letters) for i in range(10)) + '@' + random.choice(domains)
    return email

class User(AbstractBaseUser):
    temp_email = generate_random_email()
    #required by django
    email                       = models.EmailField(verbose_name="email", max_length=60, unique=True, default=temp_email)
    username                    = models.CharField(max_length=30, unique=True)
    date_joined                 = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    last_login                  = models.DateTimeField(default=timezone.now)
    is_admin                    = models.BooleanField(default=False)
    is_active                   = models.BooleanField(default=True)
    is_staff                    = models.BooleanField(default=False)
    is_superuser                = models.BooleanField(default=False)

    # additional fields from the project
    SECURITY_QUESTION_CHOICES = [
    ('1', "What is your mother's maiden name?"),
    ('2', "What is the name of your first pet?"),
    ('3', "In what city were you born?"),
    ('4', "What is the name of your favorite teacher?"),
    ('5', "What is your favorite movie?"),
    ('6', "What is the make and model of your first car?"),
    ('7', "What is the name of your childhood best friend?"),
    ('8', "What is your favorite book?"),
    ('9', "What is the name of the street you grew up on?"),
    ('10', "What is your favorite sports team?"),
    ('11', "What is your favorite color?"),
    ('12', "What is the name of the company where you had your first job?"),
    ('13', "What is the middle name of your oldest sibling?"),
    ('14', "What is the name of your favorite fictional character?"),
    ('15', "What is your favorite food?"),
    ('16', "What was the model of your first cellphone?"),
    ('17', "What is the name of the first school you attended?"),
    ('18', "What is the birthdate of your oldest cousin?"),
    ('19', "What is the name of the hospital where you were born?"),
    ('20', "What is your favorite vacation destination?"),
    ]



    password                    = models.CharField(max_length=128)
    Security_Question1          = models.CharField(max_length=130,choices=SECURITY_QUESTION_CHOICES)
    Security_Question1_answer   = models.CharField(max_length=30)
    Security_Question2          = models.CharField(max_length=130,choices=SECURITY_QUESTION_CHOICES)
    Security_Question2_answer   = models.CharField(max_length=30)
    First_name                  = models.CharField(max_length=30)
    Last_name                   = models.CharField(max_length=30)
    Phone_number                = models.CharField(max_length=30)
    Net_ID                      = models.CharField(max_length=30, blank=True)    

    class Role(models.TextChoices):
        Student = 'Student', 'Student'
        ScholarshipAdministrator = 'Scholarship Administrator','Scholarship Administrator'
        ApplicantReviewer = 'Applicant Reviewer', 'Applicant Reviewer'
        ScholarshipDonor = 'Scholarship Donor', 'Scholarship Donor'
        AuthorizedENGRStaff = 'Authorized ENGR Staff', 'Authorized ENGR Staff'
        ENGRITSupportStaff = 'ENGR IT Support Staff', 'ENGR IT Support Staff'


    role                       = models.CharField(max_length=50, choices=Role.choices)

    objects = MyUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username','Security_Question1','Security_Question1_answer','Security_Question2',
                       'Security_Question2_answer','First_name','Last_name','Phone_number','Net_ID','role']
    
    
    

    def __str__(self):
        return self.email
        
    # For checking permissions. to keep it simple all admin have ALL permissons
    def has_perm(self, perm, obj=None):
        return self.is_admin

    # Does this user have permission to view this app? (ALWAYS YES FOR SIMPLICITY)
    def has_module_perms(self, app_label):
        return True

    def save(self,*args, **kwargs):
        return super().save(*args, **kwargs)
        

class Student(User):
    class Meta:
        proxy = True

class ScholarshipAdministrator(User):
    class Meta:
        proxy = True

class ApplicantReviewer(User):
    class Meta:
        proxy = True

class ScholarshipDonor(User):
    class Meta:
        proxy = True

class AuthorizedENGRStaffent(User):
    class Meta:
        proxy = True

class ENGRITSupportStaff(User):

    class Meta:
        proxy = True

SECURITY_QUESTION_CHOICES = [
    ('q1', 'What is your mother\'s maiden name?'),
    # add more questions...
]





