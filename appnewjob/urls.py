from django.urls import path
from appnewjob import views
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('apploed_jobs/', views.apploed_jobs, name='apploed_jobs'),
    path('browse_jobseeker/', views.browse_jobseeker, name='browse_jobseeker'),
    path('changepassword/', views.changepassword, name='changepassword'),
    path('contacted_comp/', views.contacted_comp, name='contacted_comp'),
    path('create_job/', views.create_job, name='create_job'),
    path('create_resume/', views.create_resume, name='create_resume'),
    path('', views.index, name='index'),
    path('index2/', views.index2, name='index2'),
    path('intersted_jobs/', views.intersted_jobs, name='intersted_jobs'),
    path('job_detail/', views.job_detail, name='job_detail'),
    path('myprofilee1/', views.myprofilee1, name='myprofilee1'),
    path('myprofilee2/', views.myprofilee2, name='myprofilee2'),
    path('profile/', views.profile, name='profile'),
    path('shortlisted_comp/', views.shortlisted_comp, name='shortlisted_comp'),
    path('shortlisted_jobs/', views.shortlisted_jobs, name='shortlisted_jobs'),
    path('emp_bemp/', views.emp_bemp, name='emp_bemp'),
    path('emp_contacted_pro/', views.emp_contacted_pro, name='emp_contacted_pro'),
    path('emp_edit/', views.emp_edit, name='emp_edit'),
    path('emp_jobdetail/', views.emp_jobdetail, name='emp_jobdetail'),
    path('emp_posted_jobs/', views.emp_posted_jobs, name='emp_posted_jobs'),
    path('emp_profiles/', views.emp_profiles, name='emp_profiles'),
    path('emp_short_profil/', views.emp_short_profil, name='emp_short_profil'),
    path('empchangepassword/', views.empchangepassword, name='empchangepassword'),
    path('jobappliers/', views.empjobappliers, name='empjobappliers'),
    path('save/', views.resume_save, name='rsave'),
    # path('register/', views.register, name='register'),
    # path('login/', views.logins, name='login'),
    # path('logout/', views.logout, name='logout'),
    path('jobsave/', views.jobsave, name='jobsave'),
    path('jobupdate/<int:id>/', views.jobupdate, name='jobupdate')

]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
