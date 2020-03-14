from django.contrib import admin

# Register your models here.
from .models import Appliedjobs,Category,Industry,Jobtype,Country,Experience,Qualification,City,State,Functionalarea,Package,Designation,Resume,Createjob,Register,Bookmark,Shoortlist,Contacetd_Profiles,Interestedjobs,Notinterestedjobs

admin.site.register(Appliedjobs)
admin.site.register(Bookmark)
admin.site.register(Category)
admin.site.register(Createjob)
admin.site.register(City)
admin.site.register(Contacetd_Profiles)
admin.site.register(Country)
admin.site.register(Designation)
admin.site.register(Experience)
admin.site.register(Functionalarea)
admin.site.register(Industry)
admin.site.register(Interestedjobs)
admin.site.register(Jobtype)
admin.site.register(Notinterestedjobs)
admin.site.register(Package)
admin.site.register(Qualification)
admin.site.register(Register)
admin.site.register(Resume)
admin.site.register(State)
admin.site.register(Shoortlist)