from django import forms
from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import User
from userapp.models import Profile, User


class UpdateUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'email')
        exclude = ('password', 'password2')

        def __init__(self, *args, **kwargs):
            super(UpdateUserForm, self).__init__(*args, **kwargs)
            self.fields['username'].widget =forms.NumberInput(
                attrs={'class': 'form-control input-lg style_of_input', 'placeholder': 'Enter phonenumber',
                       'required': ''})
            self.fields['first_name'].widget = forms.TextInput(
                attrs={'class': 'form-control input-lg style_of_input', 'placeholder': 'Enter name', 'required': ''})
            self.fields['email'].widget = forms.EmailInput(
                attrs={'class': 'form-control input-lg style_of_input', 'placeholder': 'Enter email', 'required': ''})


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'
        exclude = ('user', 'registered_date', 'areyou', 'otp')


# class UserForm(forms.ModelForm):
#     class Meta:
#         model = User
#         fields = ('first_name', 'last_name', 'email')
#
# class ProfileForm(forms.ModelForm):
#     class Meta:
#         model = Profile
#         fields = ('url', 'location', 'company')