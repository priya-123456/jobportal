from django.shortcuts import render, redirect
from .models import Createjob, Category, City, State, Resume, \
                          Functionalarea, Jobtype, Industry, Experience, Package, Country
from .forms import ResumeForm, JobForm
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth import authenticate, logout as auth_logout, login as auth_login
from django.contrib import messages


def apploed_jobs(request):
    return render(request, 'applied_jobs.html')


def browse_jobseeker(request):
    job=Createjob.objects.all()
    return render(request, 'browse_jobseeker.html',{'job':job})


def changepassword(request):
    return render(request, 'changepassword.html')


def contacted_comp(request):
    return render(request, 'contacted_com.html')


def create_job(request):
    jform = JobForm()
    return render(request, 'create_job.html', {'jform': jform})


def jobsave(request):
    if request.method == "POST":
        jform = JobForm(request.POST, request.FILES)
        if jform.is_valid():
            jform.save()
            messages.success(request, "Job Posted Successfully........")
            return redirect(create_job)
        else:
            messages.error(request, "Job posting failed..........")
            return redirect(create_job)
    else:
        jform = JobForm()
        return render(request, "create_job.html", {'jform': jform})


def create_resume(request):

    form = ResumeForm()
    return render(request, 'create_resume.html', {'jform': form})
def resumesave(request):
    form=ResumeForm()
    if request.method=='POST':
        form = ResumeForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return render(request, 'create_resume.html', {'form': form})
        else:
            messages.error(request, "Resume posting failed..........")
            return redirect(create_resume)
    # else:
    #     jform = ResumeForm()
    #     return render(request, "create_resume.html", {'jform': jform})



# def resume_save(request):
#     if request.method == "POST":
#         rform = ResumeForm(request.POST, request.FILES)
#         if rform.is_valid():
#             rform.save()
#             messages.success(request, "resume Posted Successfully........")
#             return redirect(create_resume)
#         else:
#             messages.error(request, "reume posting failed..........")
#             return redirect(create_resume)
#     else:
#         rform = ResumeForm()
#         return render(request, "create_resume.html", {'rform': rform})


def index(request):
    return render(request, 'index.html')


def index2(request):
    return render(request, 'index2.html')


def intersted_jobs(request):
    return render(request, 'interested_jobs.html')


def job_detail(request):
    return render(request, 'job_detail.html')


def myprofilee1(request):
    return render(request, 'myprofilee1.html')


def myprofilee2(request):
    return render(request, 'myprofilee2.html')


def profile(request):
    return render(request, 'profile.html')


def shortlisted_comp(request):
    return render(request, 'shortlisted_com.html')


def shortlisted_jobs(request):
    return render(request, 'shortlisted_jobs.html')


def emp_bemp(request):
    return render(request, 'Employer_browse_employer.html')


def empchangepassword(request):
    return render(request, 'Employer_Changepassword.html')


def emp_contacted_pro(request):
    return render(request, 'Employer_Contacted_Pro.html')


def emp_edit(request):
    return render(request, 'Employer_Edit.html')


def emp_jobdetail(request):
    return render(request, 'Employer_job_detail.html')


def emp_posted_jobs(request):
    return render(request, 'Employer_Posted_Jobs.html')


def emp_profiles(request):
    return render(request, 'Employer_profile.html')


def emp_short_profil(request):
    return render(request, 'Employer_Shortlisted_Profiles.html')


def empjobappliers(request):
    return render(request, 'Employer_job_appliers.html')


def register(request):
    if request.method == 'POST':
        usernam = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        if password1 == password2:
            if User.objects.filter(username=usernam).exists():
                messages.error(request, 'Email already exists')
                return redirect(index)
            else:
                user = User.objects.create_user(username=usernam, email=email, password=password1)
                Log_User = authenticate(username=usernam, password=password1)
                auth.login(request, user)
                messages.success(request, 'Form submited successfully...')
                return redirect(index)
        else:
            messages.error(request, 'username or password are not matching')
            return redirect(index)
    else:
        return render(request, 'index.html')


def logins(request):
    if request.method == 'POST':
        uname = request.POST.get('uname')
        raw_password = request.POST.get('upass')
        user = auth.authenticate(username=uname, password=raw_password)
        if user is not None:
            auth_login(request, user)
            messages.success(request, 'Logined............')
            return redirect(index)
        else:
            messages.error(request, 'Invalid credentials............')
            return redirect(index)
    else:
        return redirect(logins)


def logout(request):
    auth_logout(request)
    return redirect(index)
