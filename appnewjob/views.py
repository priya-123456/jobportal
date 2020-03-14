from django.shortcuts import render, redirect
from .models import Createjob, Category, Designation,Package,Qualification,Functionalarea,Country,State, Jobtype, Industry, Resume, Bookmark, Experience, City, Register, Shoortlist, Appliedjobs, Interestedjobs, Notinterestedjobs
from django.shortcuts import get_object_or_404
from .forms import ResumeForm, JobForm
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth import authenticate, logout as auth_logout, login as auth_login
from django.contrib import messages


def apploed_jobs(request):
    return render(request, 'applied_jobs.html')


def browse_jobseeker(request):
    applied_jobs = Appliedjobs.objects.filter(user=request.user).values_list('id', flat=True)
    jobs = Createjob.objects.all()
    skills = request.POST.get('skills')
    exp = request.POST.get('exp')
    cit = request.POST.get('city')
    if skills:
        jobs = jobs.filter(keyskills=skills)
    if exp:
        jobs = jobs.filter(experience=exp)
    if cit:
        jobs = jobs.filter(city=cit)
    return render(request, 'browse_jobseeker.html', {'job': jobs,'applied_jobs': applied_jobs})


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
            jform_obj = jform.save()
            jform_obj.user = request.user
            jform_obj.save()
            messages.success(request, "Job Posted Successfully........")
            return redirect(index2)
        else:
            messages.error(request, "Job posting failed..........")
            return redirect(create_job)
    else:
        jform = JobForm()
        return render(request, "create_job.html", {'jform': jform})


def jobdata_edit(request, id):
    jform_obj = get_object_or_404(Createjob, id=id)
    if request.method == "POST":
        form = JobForm(request.POST, request.FILES, instance=jform_obj)
        if form.is_valid():
            form.save()
            return redirect('myprofilee2')
    else:
        form = JobForm(instance=jform_obj)
        Category_obj = Category.objects.all()
        Jobtype_obj = Jobtype.objects.all()
        Industry_obj = Industry.objects.all()
        Experience_obj = Experience.objects.all()
        pack_obj = Package.objects.all()
        desig_obj = Designation.objects.all()
        qul_obj = Qualification.objects.all()
        fun_obj = Functionalarea.objects.all()
        city_obj = City.objects.all()
        cou_obj = Country.objects.all()
        sta_obj = State.objects.all()
        return render(request, "create_job.html", {'jform': form, 'viewtab': 'Basic Details', 'Category_obj': Category_obj, 'Jobtype_obj': Jobtype_obj, 'Industry_obj': Industry_obj, 'Experience_obj': Experience_obj,
        'pack_obj': pack_obj, 'desig_obj': desig_obj, 'qul_obj': qul_obj, 'fun_obj': fun_obj, 'city_obj': city_obj, 'cou_obj': cou_obj, 'sta_obj': sta_obj})


def create_resume(request):
    rform = ResumeForm()
    return render(request, 'create_resume.html', {'rform': rform})


def resumesave(request):
    if request.method == "POST":
        rform = ResumeForm(request.POST, request.FILES)
        if rform.is_valid():
            rform_obj = rform.save()
            rform_obj.user = request.user
            rform_obj.save()
            messages.success(request, 'resume posted successfully')
            return redirect(index)
        else:
            messages.error(request, 'resume posted failure')
            return redirect(create_resume)
    else:
        rform=ResumeForm()
        return render(request, 'create_resume.html', {'rform': rform})


def resumedata_edit(request, id):
    rform_obj = get_object_or_404(Resume, id=id)
    if request.method == "POST":
        form = ResumeForm(request.POST, request.FILES, instance=rform_obj)
        if form.is_valid():
            form.save()
            return redirect('seekerprofile')
    else:
        form = ResumeForm(instance=rform_obj)
        desig_obj = Designation.objects.all()
        Jobtype_obj = Jobtype.objects.all()
        Industry_obj = Industry.objects.all()
        Experience_obj = Experience.objects.all()
        Package_obj = Package.objects.all()
        qul_obj = Qualification.objects.all()
        return render(request, "create_resume.html", {
        'rform': form, 'viewtab': 'Basic Details',  'desig_obj': desig_obj, 'Jobtype_obj': Jobtype_obj, 'Industry_obj': Industry_obj,
        'Experience_obj': Experience_obj, 'Package_obj': Package_obj, 'qul_obj': qul_obj})


def index(request):
    cat = Category.objects.all()
    km = Jobtype.objects.all()
    exp = Experience.objects.all()
    city = City.objects.all()
    return render(request, 'index.html', {'cat': cat, 'jtype': km, 'exp': exp, 'city': city})


def index2(request):
    ind = Industry.objects.all()
    jtype = Jobtype.objects.all()
    exp = Experience.objects.all()
    city = City.objects.all()
    return render(request, 'index2.html', {'ind': ind, 'jtype': jtype, 'exp': exp, 'city': city})


def intersted_jobs(request):
    mark = Shoortlist.objects.filter(user=request.user.id)
    return render(request, 'interested_jobs.html', {'ijob': mark})


def job_detail(request, id):
    jobs = Createjob.objects.get(id=id)
    interest = Interestedjobs.objects.filter(job=id, user=request.user.id)
    notintere = Notinterestedjobs.objects.filter(cjob=id, user=request.user.id)
    user = User.objects.get(id=request.user.id)
    return render(request, 'job_detail.html', {'job': jobs, 'user': user, 'interest': interest,
                                               'notinterest': notintere})


def myprofilee1(request):
    res = Resume.objects.all()
    # import ipdb;ipdb.set_trace()
    return render(request, 'myprofilee1.html', {'res': res})


def myprofilee2(request):
    jobs = Createjob.objects.all()
    return render(request, 'myprofilee2.html', {'jobs': jobs})


def profile(request, id):

    pro = Resume.objects.get(id=id)
    book = Bookmark.objects.filter(seeker=id, user=request.user.id)
    short = Shoortlist.objects.filter(seeker=id, user=request.user.id)
    user = User.objects.get(id=request.user.id)
    return render(request, 'profile.html', {'pro': pro, 'user': user, 'book': book, 'short': short})


def shortlisted_jobs(request):
    return render(request, 'shortlisted_jobs.html')


def emp_bemp(request):
    res=Resume.objects.all()
    skills = request.POST.get('skills')
    exp = request.POST.get('exp')
    cit = request.POST.get('city')
    if skills:
        res = res.filter(skills=skills)
    if exp:
        res = res.filter(experience=exp)
    if cit:
        res = res.filter(city=cit)
    return render(request, 'Employer_browse_employer.html', {'res': res})


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


def shortlisted_comp(request):
    return render(request, 'shortlisted_com.html')


def empjobappliers(request):
    return render(request, 'Employer_job_appliers.html')


def register(request):
    if request.method == 'POST':
        usernam = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        areyou = request.POST.get('areyou')
        if password1 == password2:
            if User.objects.filter(username=usernam).exists():
                messages.error(request, 'Email already exists')
                return redirect(index)
            else:
                user_object = User.objects.create_user(username=usernam, email=email, password=password1)
                Register.objects.create(user=user_object, areyou=areyou)
                user = authenticate(username=usernam, password=password1)
                if user:
                    auth_login(request, user)
                    messages.success(request, 'Registred successfully')
                    if request.user.register.areyou == "Job Seekar":
                        return redirect(index)
                    else:
                        return redirect(index2)
                messages.success(request, 'Form submited successfully...')
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
            if request.user.register.areyou == 'Job Seekar':
                return redirect(index)
            else:
                return redirect(index2)
        else:
            messages.error(request, 'Invalid credentials............')
            return redirect(index)
    else:
        return redirect(logins)


def logout(request):
    auth_logout(request)
    return redirect(index)


def catgoryfilter(request, id):
    sk = Category.objects.get(id=id)
    lm = Createjob.objects.filter(category=sk)
    return render(request, 'browse_jobseeker.html', {'job': lm})


def jobtypefilter(request, id):
    sk = Jobtype.objects.get(id=id)
    lm = Createjob.objects.filter(jobtype=sk)
    return render(request, 'browse_jobseeker.html', {'job': lm})


def indfilter(request, id):
    ind = Industry.objects.get(id=id)
    kl = Resume.objects.filter(desired_industry=ind)
    return render(request, 'Employer_browse_employer.html', {'res': kl})


def typefilter(request, id):
    sk = Jobtype.objects.get(id=id)
    lm = Resume.objects.filter(desired_job_type=sk)
    return render(request, 'browse_jobseeker.html', {'res': lm})


def bookmarksave(request):
    usrs = request.POST.get('user')
    resum = request.POST.get('resume')
    shrt = Bookmark(user_id=usrs, seeker_id=resum)
    shrt.save()
    return redirect(index)


def shortlistsave(request):
    user = request.POST.get('user')
    short = request.POST.get('short')
    shor = Shoortlist(user_id=user, seeker_id=short)
    shor.save()
    return redirect(index2)


def contactedpro(request):
    user = request.POST.get('user')
    contact = request.POST.get('short')
    conact = Shoortlist(users_id=user, contact_id=contact)
    conact.save()
    return redirect(index2)


def interested(request):
    user = request.POST.get('user')
    job = request.POST.get('ijob')
    inter = Interestedjobs(user_id=user, job_id=job)
    inter.save()
    return redirect(index)


def notinterested(request):
    user = request.POST.get('user')
    cjob = request.POST.get('njob')
    inter = Interestedjobs(user_id=user, cjob_id=cjob)
    inter.save()
    return redirect(index)


def applied(request):
    user = request.POST.get('user')
    appjob = request.POST.get('njob')
    inter = Appliedjobs(user_id=user, appjob_id=appjob)
    inter.save()
    return redirect(index)


def bookmark(request):
    bookmarks =Bookmark.objects.filter(user=request.user)
    return render(request, 'bookmarks.html', {'bmark': bookmarks})


def emp_short_profil(request):
    mark = Shoortlist.objects.filter(user=request.user)
    return render(request, 'Employer_Shortlisted_Profiles.html', {'klm': mark})




