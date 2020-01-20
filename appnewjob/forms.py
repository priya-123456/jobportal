from django import forms
from .models import Resume,Createjob

class ResumeForm(forms.ModelForm):
    class Meta:
        model=Resume
        fields="__all__"

class JobForm(forms.ModelForm):
    class Meta:
        model=Createjob
        fields="__all__"