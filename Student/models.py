from django.db import models

# Create your models here.
class Student(models.Model):
    # Basic Information
    student_info = models.OneToOneField('Login.User', on_delete=models.CASCADE, default = None)
    
    # Additional Information

    major_requirement_choices = (
        ('Engineering', 'Engineering'), 
        ('Business', 'Business'),
        ('Music', 'Music'), 
        ('Art', 'Art'),
        ('Performing Arts', 'Performing Arts'), 
        ('Theater Tech', 'Theater Tech'),
        ('Photography', 'Photography'), 
        ('Nursing', 'Nursing'), 
        ('Computer Science', 'Computer Science'), 
        ('Biology', 'Biology'), 
        ('Chemistry', 'Chemistry'), 
        ('Physics', 'Physics'), 
        ('Political Science', 'Political Science'), 
        ('Literature', 'Literature'), 
        ('Writing', 'Writing'), 
        ('Foreign Language', 'Foreign Language'),
        ('Law', 'Law'), 
        ('Medicine', 'Medicine'), 
        ('Communications', 'Communications'), 
        ('Marketing', 'Marketing'), 
        ('Finance', 'Finance'), 
        ('Ecomomics', 'Economics'), 
        ('Math', 'Math'), 
        ('Environmental Science', 'Environmental Science'), 
        ('Public Health', 'Public Health'), 
        ('Graphic Design', 'Graphic Design'), 
        ('Architecture', 'Architecture'), 
        ('Education', 'Education'), 
        ('Astronomy', 'Astronomy'), 
        ('Social Sciences', 'Social Sciences'), 
        ('Fashion', 'Fashion'), 
        ('Statistics', 'Statistics'),
        ('Geology', 'Geology'), 
        ('Neuroscience', 'Neuroscience'),
        ('Psychology', 'Psychology'),
        ('none', 'none'),
    )

    preferred_pronoun = models.CharField(max_length=20, blank=True, null=True)
    major = models.CharField(max_length=30 ,choices = major_requirement_choices)
    minor = models.CharField(max_length=30 ,choices = major_requirement_choices, blank=True, null=True)
    gpa = models.DecimalField(max_digits=3, decimal_places=2, blank=True, null=True)
    current_year_choices = [
        ('Freshman', 'Freshman'),
        ('Sophomore', 'Sophomore'),
        ('Junior', 'Junior'),
        ('Senior', 'Senior'),
        ('Graduate', 'Graduate'),
    ]
    current_year = models.CharField(max_length=20, choices=current_year_choices)
    ethnicity_choices = [
        ('Caucasian', 'Caucasian'),
        ('Hispanic', 'Hispanic'),
        ('Black', 'Black'),
        ('European', 'European'),
        ('Asian', 'Asian'),
        ('Indian', 'Indian'),
        ('American Indian', 'American Indian'),
        ('Arabic/Middle Eastern', 'Arabic/Middle Eastern'),
        ('Other', 'Other'),
    ]
    ethnicity = models.CharField(max_length=30, choices=ethnicity_choices)
    personal_statement_essay = models.TextField()
    work_experience = models.TextField()

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.username}"
