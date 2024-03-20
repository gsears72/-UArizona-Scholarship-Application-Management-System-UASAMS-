# forms.py
from typing import Any
from django import forms
from ScholarshipDonor.models import Scholarship

class ScholarshipForm(forms.ModelForm):
    class Meta:
        model = Scholarship
        fields = '__all__'
        widgets = {
            'scholarship_name': forms.TextInput(attrs={'class': 'form-control', 'id': 'name'}),
            'scholarship_amount': forms.NumberInput(attrs={'class': 'form-control', 'id': 'amount'}),
            'donor_full_name': forms.TextInput(attrs={'class': 'form-control', 'id': 'donor_full_name'}),
            'donor_phone_number': forms.TextInput(attrs={'class': 'form-control', 'id': 'donor_phone_number'}),
            'donor_email': forms.EmailInput(attrs={'class': 'form-control', 'id': 'donor_email'}),
            'num_scholarships_available': forms.NumberInput(attrs={'class': 'form-control', 'id': 'num_scholarships_available'}),
            'required_majors_or_minors': forms.TextInput(attrs={'class': 'form-control', 'id': 'required_majors_or_minors'}),
            'required_gpa': forms.NumberInput(attrs={'class': 'form-control', 'id': 'required_gpa', 'step': '0.01'}),
            'application_deadline': forms.DateInput(attrs={'class': 'form-control', 'id': 'application_deadline', 'type': 'date'}),
            'other_requirements': forms.Textarea(attrs={'class': 'form-control', 'id': 'other_requirements', 'rows': 3}),
        }
