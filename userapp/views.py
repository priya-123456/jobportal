from django.shortcuts import render, redirect
from .models import Profile
from .forms import ProfileUpdateForm, UpdateUserForm, UserCreationForm
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.models import User
import json
from datetime import datetime, timedelta
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate
from django.contrib import auth
# Create your views here.

# def update_profile(request, user_id):
#     user = User.objects.get(pk=user_id)
#     user.profile.bio = 'Lorem ipsum dolor sit amet, consectetur adipisicing elit...'
#     user.save()
#
# # @login_required
# # @transaction.atomic
# def update_profile(request):
#     if request.method == 'POST':
#         user_form = UpdateUserForm(request.POST, instance=request.user)
#         profile_form = ProfileUpdateForm(request.POST, instance=request.user.profile)
#         if user_form.is_valid() and profile_form.is_valid():
#             user_form.save()
#             profile_form.save()
#             messages.success(request, _('Your profile was successfully updated!'))
#             return redirect('settings:profile')
#         else:
#             messages.error(request, _('Please correct the error below.'))
#     else:
#         user_form = UpdateUserForm(instance=request.user)
#         profile_form = ProfileUpdateForm(instance=request.user.profile)
#     return render(request, 'index.html', {
#         'user_form': user_form,
#         'profile_form': profile_form
#     })



def register(request):
    if request.method == 'POST':
        first_name = request.POST.get("first_name")
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        password2 = request.POST.get("password2")
        areyou = request.POST.get("areyou")
        status = 'success'
        icon = 'success'
        resp = None
        User.objects.filter(is_active=False, date_joined__lte=datetime.now() - timedelta(minutes=10)).delete()
        if password == password2:
            try:
                User.objects.get(username=username)
                messages.success(request, "Mobile Number already exist")
                status = 'failed'
                icon = 'error'
            except:
                try:
                    fb = ''
                    user_object = User.objects.create(first_name=first_name, username=username, email=email,
                                                      password=make_password(password), is_active=False)
                    Profile.objects.create(user=user_object, fb_id=fb, areyou=areyou)
                    # message = 'Verify you account with otp...'
                    resp = user_object.id
                except Exception as e:
                    status = 'failed'
                    icon = 'error'
                    message = 'please fix follwoing issues {}'.format(e)
            resp={
                    'status': status,
                    # 'mesg': message,
                    'resp': resp,
                    'icon': icon,
                }
        else:
            messages.error("Passwords must match")
    return HttpResponse(json.dumps(resp))

#
# def login(request):
#     if request.method == 'POST':
#         username = request.POST.get("username")
#         password = request.POST.get("password")
#         user = authenticate(username=username, password=pasword)
#         if not user:
#             user = User.objects.get(username=email)
#             user = authenticate(username=username.user_object)


