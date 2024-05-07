from typing import Any
from django import forms 
from Student.models import Student
from Login.models import User


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

current_year_choices = [
        ('Freshman', 'Freshman'),
        ('Sophomore', 'Sophomore'),
        ('Junior', 'Junior'),
        ('Senior', 'Senior'),
        ('Graduate', 'Graduate'),
    ]

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



class StudentForm(forms.ModelForm):
    class Meta:
        model = Student 
        fields = '__all__'
        widgets = {
            'preferred_pronoun': forms.TextInput(attrs={'class': 'form-control', 'id': 'pronoun'}),
            'ethnicity': forms.Select(choices=ethnicity_choices,attrs={'class': 'form-control', 'id': 'ethnicity'}),
            'current_year': forms.Select(choices=current_year_choices,attrs={'class': 'form-control', 'id': 'year'}),
            'major': forms.Select(choices=major_requirement_choices,attrs={'class': 'form-control', 'id': 'major'}),
            'minor': forms.Select(choices=major_requirement_choices,attrs={'class': 'form-control', 'id': 'minor'}),
            'gpa': forms.NumberInput(attrs={'class': 'form-control', 'id': 'gpa'}),
            'work_experience': forms.Textarea(attrs={'class': 'form-control', 'id': 'work', 'rows':3}),
            'personal_statement_essay': forms.Textarea(attrs={'class': 'form-control', 'id': 'essay', 'rows':3}),
        }

class UserForm(forms.ModelForm):
    class Meta: 
        model = User
        fields = '__all__'
        widgets = {
            'First_name': forms.TextInput(attrs={'class': 'form-control', 'id': 'first_name'}),
            'Last_name': forms.TextInput(attrs={'class': 'form-control', 'id': 'last_name'}),
            'username': forms.TextInput(attrs={'class': 'form-control', 'id': 'username'}),
            'password': forms.TextInput(attrs={'class': 'form-control', 'id': 'password'}),
            'Net_ID': forms.TextInput(attrs={'class': 'form-control', 'id': 'netID'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'id': 'email'}),
            'Phone_number': forms.TextInput(attrs={'class': 'form-control', 'id': 'phone'}),
            'Security_Question1': forms.Select(choices=SECURITY_QUESTION_CHOICES,attrs={'class': 'form-control', 'id': 'q1'}),
            'Security_Question1_answer': forms.TextInput(attrs={'class': 'form-control', 'id': 'q1a'}),
            'Security_Question2': forms.Select(choices=SECURITY_QUESTION_CHOICES,attrs={'class': 'form-control', 'id': 'q2'}),
            'Security_Question2_answer': forms.TextInput(attrs={'class': 'form-control', 'id': 'q2a'}),
        }

class UploadFileForm(forms.Form):
    file = forms.FileField(required=False, widget=forms.FileInput(attrs={'class':'form-control', 'id': 'file'}))
