from typing import Any
from django import forms
from django.contrib.auth.forms import UserCreationForm
from Login.models import User






class CreateStudentForm(UserCreationForm):
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

    # Define form fields with corresponding widgets and attributes
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))  
    username = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    Security_Question1 = forms.ChoiceField(choices=SECURITY_QUESTION_CHOICES, widget=forms.Select(attrs={'class': 'form-control'})) 
    Security_Question1_answer = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))     
    Security_Question2 = forms.ChoiceField(choices=SECURITY_QUESTION_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    Security_Question2_answer = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))   
    First_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    Last_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    Phone_number = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    Net_ID = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['email', 'username', 'Security_Question1', 'Security_Question1_answer',
                   'Security_Question2', 'Security_Question2_answer', 'First_name', 'Last_name',
                   'Phone_number', 'Net_ID', 'role']
        
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super(CreateStudentForm, self).__init__(*args, **kwargs)
        self.fields['role'].widget = forms.HiddenInput()
        self.fields['role'].initial = "Student"
        self.fields['password1'].label = "Password"
        self.fields['password2'].label = "Confirm Password"
        self.fields['Security_Question1'].label = "Security Question 1"
        self.fields['Security_Question1_answer'].label = "Security Question 1 Answer"
        self.fields['Security_Question2'].label = "Security Question 2"
        self.fields['Security_Question2_answer'].label = "Security Question 2 Answer"
        self.fields['First_name'].label = "First Name"
        self.fields['Last_name'].label = "Last Name"
        self.fields['Phone_number'].label = "Phone Number"
        self.fields['Net_ID'].label = "Net ID"
        self.fields['username'].widget.attrs.update({'autocomplete': 'off'})
        self.fields['password1'].widget.attrs.update({'autocomplete': 'off'})

class CreateApplicantReviewerForm(UserCreationForm):
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

    # Define form fields with corresponding widgets and attributes
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))  
    username = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    Security_Question1 = forms.ChoiceField(choices=SECURITY_QUESTION_CHOICES, widget=forms.Select(attrs={'class': 'form-control'})) 
    Security_Question1_answer = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))     
    Security_Question2 = forms.ChoiceField(choices=SECURITY_QUESTION_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    Security_Question2_answer = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))   
    First_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    Last_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    Phone_number = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    Net_ID = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['email', 'username', 'Security_Question1', 'Security_Question1_answer',
                   'Security_Question2', 'Security_Question2_answer', 'First_name', 'Last_name',
                   'Phone_number', 'Net_ID', 'role']
        
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super(CreateStudentForm, self).__init__(*args, **kwargs)
        self.fields['role'].widget = forms.HiddenInput()
        self.fields['role'].initial = "Applicant Reviewer"
        self.fields['password1'].label = "Password"
        self.fields['password2'].label = "Confirm Password"
        self.fields['Security_Question1'].label = "Security Question 1"
        self.fields['Security_Question1_answer'].label = "Security Question 1 Answer"
        self.fields['Security_Question2'].label = "Security Question 2"
        self.fields['Security_Question2_answer'].label = "Security Question 2 Answer"
        self.fields['First_name'].label = "First Name"
        self.fields['Last_name'].label = "Last Name"
        self.fields['Phone_number'].label = "Phone Number"
        self.fields['Net_ID'].label = "Net ID"
        self.fields['username'].widget.attrs.update({'autocomplete': 'off'})
        self.fields['password1'].widget.attrs.update({'autocomplete': 'off'})


class CreateScholorshipAdministratorForm(UserCreationForm):
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

    # Define form fields with corresponding widgets and attributes
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))  
    username = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    Security_Question1 = forms.ChoiceField(choices=SECURITY_QUESTION_CHOICES, widget=forms.Select(attrs={'class': 'form-control'})) 
    Security_Question1_answer = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))     
    Security_Question2 = forms.ChoiceField(choices=SECURITY_QUESTION_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    Security_Question2_answer = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))   
    First_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    Last_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    Phone_number = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    Net_ID = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['email', 'username', 'Security_Question1', 'Security_Question1_answer',
                   'Security_Question2', 'Security_Question2_answer', 'First_name', 'Last_name',
                   'Phone_number', 'Net_ID', 'role']
        
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super(CreateStudentForm, self).__init__(*args, **kwargs)
        self.fields['role'].widget = forms.HiddenInput()
        self.fields['role'].initial = "Scholorship Administrator"
        self.fields['password1'].label = "Password"
        self.fields['password2'].label = "Confirm Password"
        self.fields['Security_Question1'].label = "Security Question 1"
        self.fields['Security_Question1_answer'].label = "Security Question 1 Answer"
        self.fields['Security_Question2'].label = "Security Question 2"
        self.fields['Security_Question2_answer'].label = "Security Question 2 Answer"
        self.fields['First_name'].label = "First Name"
        self.fields['Last_name'].label = "Last Name"
        self.fields['Phone_number'].label = "Phone Number"
        self.fields['Net_ID'].label = "Net ID"
        self.fields['username'].widget.attrs.update({'autocomplete': 'off'})
        self.fields['password1'].widget.attrs.update({'autocomplete': 'off'})


class CreateScholorshipDonorForm(UserCreationForm):

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

    # Define form fields with corresponding widgets and attributes
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))  
    username = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    Security_Question1 = forms.ChoiceField(choices=SECURITY_QUESTION_CHOICES, widget=forms.Select(attrs={'class': 'form-control'})) 
    Security_Question1_answer = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))     
    Security_Question2 = forms.ChoiceField(choices=SECURITY_QUESTION_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    Security_Question2_answer = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))   
    First_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    Last_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    Phone_number = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['email', 'username', 'Security_Question1', 'Security_Question1_answer',
                   'Security_Question2', 'Security_Question2_answer', 'First_name', 'Last_name',
                   'Phone_number', 'role']
        
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super(CreateStudentForm, self).__init__(*args, **kwargs)
        self.fields['role'].widget = forms.HiddenInput()
        self.fields['role'].initial = "Scholorship Donor"
        self.fields['password1'].label = "Password"
        self.fields['password2'].label = "Confirm Password"
        self.fields['Security_Question1'].label = "Security Question 1"
        self.fields['Security_Question1_answer'].label = "Security Question 1 Answer"
        self.fields['Security_Question2'].label = "Security Question 2"
        self.fields['Security_Question2_answer'].label = "Security Question 2 Answer"
        self.fields['First_name'].label = "First Name"
        self.fields['Last_name'].label = "Last Name"
        self.fields['Phone_number'].label = "Phone Number"
        self.fields['username'].widget.attrs.update({'autocomplete': 'off'})
        self.fields['password1'].widget.attrs.update({'autocomplete': 'off'})
       


