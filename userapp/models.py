from django.db import models
from django.contrib.auth.models import User, AbstractBaseUser
from django.db.models.signals import post_save
from django.dispatch import receiver
import requests
from random import randint

# Create your models here.
Areyou = (('Employer', 'Employer'), ('Job seeker', 'Job seeker'))

def generateOTP(mobilenumber) :
    OTP = randint(100000, 999999)
    OTP = 12345
    # message ="your one time password is {}, please dont share with any one".format(OTP)
#     URL = "https://www.bulksmsgateway.in/sendmessage.php"
#     PARAMS = {
#                 'user':'Hydevents',
#                 'password':'Hyd@0987=',
#                 'mobile':mobilenumber,
#                 'message':message,
#                 'sender':'HYDEVT',
#                 'type':'3',
#             }
#     r = requests.get(url=URL, params=PARAMS)
#     data = r.json()
    return OTP



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    pic = models.FileField(upload_to='profilepics/', blank=True, null=True)
    areyou = models.CharField(max_length=64, default='job seeker', choices=Areyou)
    # otp = models.IntegerField()
    fb_id = models.CharField(max_length=300, blank=True)
    registered_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username

    # @receiver(post_save, sender=User)
    # def create_user_profile(sender, instance, created, **kwargs):
    #     if created:
    #         Profile.objects.create(user=instance)
    #
    # @receiver(post_save, sender=User)
    # def save_user_profile(sender, instance, **kwargs):
    #     instance.profile.save()
