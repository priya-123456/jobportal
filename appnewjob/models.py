from django.db import models


class Category(models.Model):
    cat = models.CharField(max_length=30)
    catimg = models.FileField(upload_to='catimg')

    def __str__(self):
        return self.cat


class Industry(models.Model):
    industry = models.CharField(max_length=40)
    indimg = models.FileField(upload_to='indimg/')

    def __str__(self):
        return self.industry


class Jobtype(models.Model):
    jobtype = models.CharField(max_length=15)
    jobimg = models.FileField(upload_to='jonimg/')

    def __str__(self):
        return self.jobtype


class Country(models.Model):
    country = models.CharField(max_length=50)

    def __str__(self):
        return self.country


class Experience(models.Model):
    experience = models.CharField(max_length=50)

    def __str__(self):
        return self.experience


class Qualification(models.Model):
    qulification = models.CharField(max_length=25)

    def __str__(self):
        return self.qulification


class City(models.Model):
    city = models.CharField(max_length=50)

    def __str__(self):
        return self.city


class State(models.Model):
    state = models.CharField(max_length=50)

    def __str__(self):
        return self.state


# class Specialization(models.Model):
#     special = models.CharField(max_length=100)

#     def __str__(self):
#         return self.special


class Functionalarea(models.Model):
    functionalarea = models.CharField(max_length=150)

    def __str__(self):
        return self.functionalarea


class Package(models.Model):
    package = models.CharField(max_length=25)

    def __str__(self):
        return self.package


class Designation(models.Model):
    desg = models.CharField(max_length=50)

    def __str__(self):
        return self.desg


Gender = (('male', 'Male'), ('female', 'Female'), ('other', 'Other'))

Passport = (('yes', 'Yes'), ('no', 'No'))

Marrital_status = (('unmarried', 'Unmarried'), ('married', 'Married'))

Shifts = (('Day shift', 'Day shift'), ('Night shift', 'Night shift'), ('Rotational shift', 'Rotational shift'))

avaltojoin = (('Immediatly', 'Immediatly'), ('Within 15days', 'Within 15days'), ('1 month', '1 month'),
              ('2 months', '2 months'),
              ('3 months', '3 months'), ('4 months', '4 months'), ('5 months', '5 months'), ('6 months', '6 months '))

Hiringprocess = (('Face to Face', 'Face to Face'), ('Written Test', 'Written Test'), ('Telephonic', 'Telephonic'),
                 ('Group Discussion', 'Group Discussion'), ('Walk in', 'Walk in'))

Eligiblefor = (('Male candidates only', 'Male candidates only'), ('Female candidates only', 'Female candidates only'),
               ('both male and female candidates', 'both male and female candidates'))


class Resume(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    mobile_number = models.IntegerField()
    date_of_birth = models.DateField()
    resume = models.FileField(upload_to='resumes/')
    uploadyourpic=models.FileField(upload_to='pics')
    passport = models.CharField(max_length=20, choices=Passport)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=25)
    father_name = models.CharField(max_length=50)
    hobbies = models.CharField(max_length=70)
    languages_known = models.CharField(max_length=150)
    gender = models.CharField(max_length=15, choices=Gender)
    marital_status = models.CharField(max_length=25, choices=Marrital_status)
    career = models.CharField(max_length=300)
    desired_job_title = models.CharField(max_length=30)
    desired_job_type = models.ForeignKey(Jobtype, on_delete=models.CASCADE)
    designation = models.ForeignKey(Designation, on_delete=models.CASCADE)
    # total_work_experience=models.ForeignKey(Experience, on_delete=models.CASCADE)
    expect_package = models.ForeignKey(Package, on_delete=models.CASCADE)
    desired_shift = models.CharField(max_length=30, choices=Shifts)
    desired_location = models.CharField(max_length=50)
    desired_industry = models.ForeignKey(Industry, on_delete=models.CASCADE)
    availability_to_join = models.CharField(max_length=25, choices=avaltojoin)
    qualification = models.ForeignKey(Qualification, on_delete=models.CASCADE)
    university_name_collage_name_school_name = models.CharField(max_length=50)
    # specialization = models.ForeignKey(Specialization,on_delete=models.CASCADE)
    year_of_passing = models.DateField()
    percentage = models.CharField(max_length=5)
    skills = models.CharField(max_length=70)
    experience = models.ForeignKey(Experience, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=40)
    job_description = models.CharField(max_length=400)
    facebook_account = models.URLField()
    google_account = models.URLField()
    twitter_account = models.URLField()
    linkedin_account = models.URLField()
    pinterest_account = models.URLField()
    instagram_account = models.URLField()

    def __str__(self):
        return self.first_name


class Createjob(models.Model):
    jobtitle = models.CharField(max_length=50)
    designation = models.ForeignKey(Designation, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    industry = models.ForeignKey(Industry, on_delete=models.CASCADE)
    funarea = models.ForeignKey(Functionalarea, on_delete=models.CASCADE)
    hiringprocess = models.CharField(max_length=50, choices=Hiringprocess)
    experience = models.ForeignKey(Experience, on_delete=models.CASCADE)
    no_of_vac = models.CharField(max_length=25)
    package = models.ForeignKey(Package, on_delete=models.CASCADE)
    jobtype = models.ForeignKey(Jobtype, on_delete=models.CASCADE)
    joblocation = models.CharField(max_length=60)
    keyskills = models.CharField(max_length=60)
    educationqul = models.ForeignKey(Qualification, on_delete=models.CASCADE)
    yofpass = models.CharField(max_length=40)
    qulmarks = models.CharField(max_length=20)
    languages = models.CharField(max_length=100)
    eligiblefor = models.CharField(max_length=40, choices=Eligiblefor)
    flexiblefor = models.CharField(max_length=50, choices=Shifts)
    type_of_company = models.CharField(max_length=30)
    comapnyname = models.CharField(max_length=100)
    cemail = models.CharField(max_length=50)
    cnumber = models.IntegerField()
    altermbl = models.IntegerField()
    website = models.URLField()
    address = models.CharField(max_length=100)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    Country = models.ForeignKey(Country, on_delete=models.CASCADE)
    zipcode = models.IntegerField()
    company_logo = models.FileField(upload_to='logos/')
    interview_location = models.CharField(max_length=100)
    contact_person_role = models.CharField(max_length=25)
    contact_person_name = models.CharField(max_length=25)
    cont_per_ofmail = models.EmailField()
    job_summary = models.CharField(max_length=400)
    responsibilities = models.CharField(max_length=400)
    benifits = models.CharField(max_length=400)
    company_descrption = models.CharField(max_length=300)
    facebook = models.URLField()
    google = models.URLField()
    twitter = models.URLField()
    linkedin = models.URLField()
    pinterest = models.URLField()
    instagram = models.URLField()

    def __str__(self):
        return self.comapnyname
