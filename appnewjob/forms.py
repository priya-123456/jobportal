
from django import forms
from .models import Resume, Createjob, Bookmark
import django_filters


class ResumeForm(forms.ModelForm):
    class Meta:
        model = Resume
        fields = "__all__"
        exclude = ('user',)


class JobForm(forms.ModelForm):
    class Meta:
        model = Createjob
        fields = "__all__"
        exclude = ('user',)


# class BookFilter(django_filters.FilterSet):
#     class Meta:
#         model = Bookmark
#         fields = ('user', 'seeker')
