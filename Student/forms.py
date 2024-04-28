from django import forms

class UploadFileForm(forms.Form):
    resume = forms.FileField()

    class Meta:
        fields = ['resume'] 