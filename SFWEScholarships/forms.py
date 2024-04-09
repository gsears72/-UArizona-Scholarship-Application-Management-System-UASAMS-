from django import forms
from .models import Application

class ApplicationForm(forms.ModelForm):

    personal_statement = forms.CharField(max_length= 1000, required=True, widget=forms.Textarea(attrs={'class':'form-control'}))

    class Meta:
        model = Application
        fields = ['scholarship', 'student', 'stauts', 'personal_statement']  
        
