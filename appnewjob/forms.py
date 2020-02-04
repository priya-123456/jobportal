
from django import forms
from .models import Resume, Createjob
from appnewjob.data import Gender
from django.forms.widgets import DateInput,RadioSelect

class ResumeForm(forms.ModelForm):
    class Meta:
        model = Resume
        fields = "__all__"


class JobForm(forms.ModelForm):
    class Meta:
        model = Createjob
        fields = "__all__"