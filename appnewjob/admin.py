from django.contrib import admin
from .models import Category, Industry, Jobtype, Country, Experience, Qualification, City,\
    State, Functionalarea, Package, Designation, Resume, Createjob,Shortlist


admin.site.register(Category)
admin.site.register(Industry)
admin.site.register(Jobtype)
admin.site.register(Country)
admin.site.register(Experience)
admin.site.register(Qualification)
admin.site.register(City)
admin.site.register(State)
# admin.site.register(Specialization)
admin.site.register(Functionalarea)
admin.site.register(Package)
admin.site.register(Designation)
admin.site.register(Resume)
admin.site.register(Createjob)
admin.site.register(Shortlist)

