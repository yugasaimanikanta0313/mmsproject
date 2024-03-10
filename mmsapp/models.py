from django.db import models
# from django.db.models import Model
from django.urls import reverse


class Course(models.Model):
    course_id = models.AutoField(primary_key=True)
    course_code = models.CharField(blank=False,max_length=100)
    course_title = models.CharField(blank=False,max_length=200)
    course_credits = models.IntegerField(blank=False)

    class Meta:
        db_table = "course_table"

    def __str__(self):
        return self.course_code + ' ' + self.course_title



class Student(models.Model):
    id=models.AutoField(primary_key=True)
    fullname=models.CharField(max_length=100,blank=False)
    dep_choices = ( ("CSE","Computer Science") , ("Mech","Mechanical") , ("AI & DS","Artificial Intelligence") )
    department= models.CharField(blank=False,choices=dep_choices,max_length=10)
    dateofbirth = models.CharField(blank=False,max_length=20)
    email=models.EmailField(max_length=100,blank=False,unique=True)
    username=models.CharField(max_length=100,blank=False,unique=True)
    password = models.CharField(max_length=100, blank=False)#default="klu123")
    contact = models.BigIntegerField(blank=False, unique=True)
    location = models.CharField(max_length=100, blank=False)
    registrationtime=models.DateTimeField(blank=False,auto_now=True)


    studentimage = models.FileField(blank=False,upload_to='studentimages')

    class Meta:
        db_table = "registration_table"


    def __str__(self):
        return self.username + ' '+ str(self.id)




class Department(models.Model):
    dept_id = models.PositiveIntegerField(primary_key=True)
    dept_name = models.CharField(max_length=50,blank=False)
    dept_hod = models.CharField(max_length=50,blank=False)
    location_choices=(  ("C-Block","Computer Block") , ("M-Block","Mechanical Block") , ("R&D Block","R&D Block")   )
    dept_location = models.CharField(max_length=50,blank=False, choices=location_choices)

    class Meta:
        db_table = "department_table"

    def __str__(self):

        return self.dept_name


class Faculty(models.Model):
    id=models.AutoField(primary_key=True)
    fullname=models.CharField(max_length=100,blank=False)
    gender_choices = ( ("M","Male") , ("F","Female") , ("Others","Prefer not to say") )
    gender=models.CharField(blank=False,choices=gender_choices,max_length=10)
    dateofbirth = models.CharField(blank=False,max_length=20)
    email=models.EmailField(max_length=100,blank=False,unique=True)
    username=models.CharField(max_length=100,blank=False,unique=True)
    password = models.CharField(max_length=100, blank=False,default="klu123")
    contact = models.BigIntegerField(blank=False, unique=True)
    qualification = models.CharField(max_length=100, blank=False)
    registrationtime=models.DateTimeField(blank=False,auto_now=True)

    class Meta:
        db_table = "Faculty_registration_table"

    def __str__(self):
        return self.username






"""class Student(models.Model):
    id = models.ForeignKey(Registration, on_delete=models.CASCADE)
    fullname = models.ForeignKey(Registration, on_delete=models.CASCADE)
    dateofbirth = models.ForeignKey(Registration, on_delete=models.CASCADE)
    gender = models.ForeignKey(Registration, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)

    class Meta:
        db_table = "student_table"

class Subject(models.Model):

    id = models.ForeignKey(Registration, on_delete=models.CASCADE)
    fullname = models.ForeignKey(Registration, on_delete=models.CASCADE)

    class Meta:
        db_table = "subject_table"

class Mark(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    mark = models.IntegerField()
    date = models.DateField(auto_now_add=True)

    class Meta:
        db_table = "marks_table" """



"""class Subject(models.Model):

    details = models.ForeignKey(Registration, default= 1, verbose_name="fullname" ,on_delete=models.CASCADE)

    sub_id = models.AutoField(primary_key=True)

    subject_choices = (("PFSD", "Python full stack"), ("MP", "Mathematical programming"), ("OS", "Operating System"))

    subject1 = models.CharField(blank=False,choices=subject_choices,max_length=10)
    subject2 = models.CharField(blank=False, choices=subject_choices, max_length=10)
    subject3 = models.CharField(blank=False, choices=subject_choices, max_length=10)

    class Meta:
        db_table = "add_subject" """


"""class Course(models.Model):
    course_id = models.AutoField(primary_key=True)
    course_code = models.CharField(blank=False,max_length=100)
    course_title = models.CharField(blank=False,max_length=200)
    course_credits = models.IntegerField(blank=False)

    class Meta:
        db_table = "course_table"  """




'''class Student_Course(models.Model):
    id = models.AutoField(primary_key=True)
    fk = models.ForeignKey(Student,on_delete=models.CASCADE)
    fk2 = models.ForeignKey(Course,on_delete=models.CASCADE)

    class Meta:
        db_table="Studentcourse_table"

 def fullname(self):
        return self.fk.username

    def course_title(self):
        return self.fk2.course_code '''




class Faculty_Course(models.Model):
    id = models.AutoField(primary_key=True)
    fk = models.ForeignKey(Faculty,on_delete=models.CASCADE)
    fk2 = models.ForeignKey(Course,on_delete=models.CASCADE)

    def f_fullname(self):
        return self.fk.f_fullname

    def course_title(self):
        return self.fk2.course_title

    class Meta:
        db_table="Facultycourse_table"



class Admin(models.Model):
    id=models.AutoField(primary_key=True)
    username=models.CharField(max_length=50,unique=True,blank=False)
    password = models.CharField(max_length=50,blank=False)

    def __str__(self):
        return self.username




class StudentMarks(models.Model):
    name = models.ForeignKey(Student,on_delete=models.CASCADE)
    roll_number = models.IntegerField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('student-detail', kwargs={'pk': self.pk})

class Marks(models.Model):
    id=models.AutoField(primary_key=True)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject = models.ForeignKey(Course,on_delete=models.CASCADE)
    marks_obtained = models.IntegerField()

    def __str__(self):
        return f'{self.student.username} - {self.subject}: {self.marks_obtained}'

    def get_absolute_url(self):
        return reverse('student-detail', kwargs={'pk': self.student.pk})

    class Meta:
        db_table="Marks_table"