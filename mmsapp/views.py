from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.http import QueryDict
from django.views.generic import ListView
from django.contrib import messages
from django.db.models import Sum
from matplotlib import pyplot as plt

from .forms import RegistrationForm, DepartmentForm, UpdateDepartmentForm, CourseForm, \
    FacultyForm, AdminLoginForm, MarkForm, MarksForm

from .models import  Department, Faculty, Student, Course, Admin, Marks


def indexfunction(request):
    return render(request,"index.html")

def formdemofunction(request):
    return render(request,"formdemo.html")

def displayformdatafunction(request):
    if request.method == "POST":
        id=request.POST['id']
        name=request.POST['name']
        gender = request.POST['gender']
        dateofbirth = request.POST['dateofbirth']
        department = request.POST['department']
        emailid = request.POST['emailid']
        contactno = request.POST['contactno']
        return render(request,"displayform.html",{"id":id,"name":name,"gender":gender,"dob":dateofbirth,"dept":department,"email":emailid,"contactno":contactno})
    if request.method == "GET":
        id = request.GET['id']
        name = request.GET['name']
        gender = request.GET['gender']
        dateofbirth = request.GET['dateofbirth']
        department = request.GET['department']
        emailid = request.GET['emailid']
        contactno = request.GET['contactno']
        return render(request, "displayform.html",{"id": id, "name": name, "gender": gender, "dob": dateofbirth, "dept": department,"email": emailid, "contactno": contactno})

def logindemofunction(request):
    return render(request,"logindemo.html")

def checklogindemofunction(request):
    email = request.POST['emailid']
    pwd = request.POST['password']
    if email=="klu@gmail.com" and pwd=="klu":
        return HttpResponse("<b>Login Success</b>")
    else:
        return HttpResponse("<font color=red>Login Failed</font>")

def addemployeefunction(request):
    return render(request,"addemployee.html")

'''def saveemployeefunction(request):
    id = request.POST['id']
    name = request.POST['name']
    gender = request.POST['gender']
    dateofbirth = request.POST['dateofbirth']
    department = request.POST['department']
    emailid = request.POST['emailid']
    contactno = request.POST['contactno']
    employeeobj = Employee(emp_id=id,emp_name=name,emp_gender=gender,emp_dob=dateofbirth,emp_dept=department,emp_email=emailid,emp_contactno=contactno)
    Employee.save(employeeobj)
    return HttpResponse("Employee Added Successfully") '''

def registration(request):
    form = RegistrationForm()
    if request.method == "POST":
        form = RegistrationForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            msg="Successfully Registered"
            return render(request,"registration.html",{"form":form,"msg":msg})
            form = RegistrationForm()
        else:
            print(form.errors)
            return HttpResponse("Registraion Failed")
    return render(request,"registration.html",{"form":form})

def userlogin(request):
    return render(request,"userlogin.html")

def checkuserlogin(request):
    emailid = request.POST["emailid"]
    pwd = request.POST["password"]

    flag = Student.objects.filter(Q(email=emailid) & Q(password=pwd)) #faculty_registration.objects.filter(Q(f_email=emailid) & Q(f_password=pwd)) )
    print(flag)

    if flag:
        user= Student.objects.get(email=emailid)
        print(user)
        print(user.id,user.fullname,user.department) #other fields also
        request.session["uname"]=user.username
        return render(request,"userhome.html",{"uname":user.username})
    else:
        msg="Login Failed"
        return render(request,"userlogin.html",{"msg":msg})

def userhome(request):
    uname=request.session["uname"]
    return render(request,"userhome.html",{"uname":uname})

def userlogout(request):
    return render(request,"userlogin.html")

def viewusers(request):
    usersdata = Student.objects.all()
    userscount = Student.objects.count()
    return render(request,"viewusers.html",{"users":usersdata,"count":userscount})

def adddepartment(request):
    form=DepartmentForm()

    if request.method == "POST":
        form=DepartmentForm(request.POST)
        if form.is_valid():
            form.save()
            msg="Department Added Successfully"
            return render(request,"adddepartment.html",{"msg":msg,"deptform":form})
        else:
            msg="Failed to Add Department"
            return render(request, "adddepartment.html", {"msg": msg,"deptform":form})

    return render(request,"adddepartment.html",{"deptform":form})


'''def updatdepartment(request):
    form = UpdateDepartmentForm()

    if request.method == "POST":
        form=UpdateDepartmentForm(request.POST)

        id=form.data["dept_id"]
        hod = form.data["dept_hod"]
        location = form.data["dept_location"]

        flag=Department.objects.filter(dept_id=id)

        if flag:
            Department.objects.filter(dept_id=id).update(dept_hod=hod,dept_location=location)
            msg="Department Updated Successfully"
            return render(request, "updatedepartment.html", {"deptform": form,"msg":msg})
        else:
            msg="Department ID Not Found"
            return render(request, "updatedepartment.html", {"deptform": form, "msg": msg})

    else:
        return render(request,"updatedepartment.html",{"deptform":form})



    return render(request,"updatedepartment.html",{"deptform":form}) '''


def deleteuser(request,uid):
    Student.objects.filter(id=uid).delete()
    return redirect("viewusers")


def deletefaculty(request,uid):
    Faculty.objects.filter(id=uid).delete()
    return redirect("viewfaculty")


def faculty_registration(request):
    form = FacultyForm()
    if request.method == "POST":
        form = FacultyForm(request.POST)
        if form.is_valid():
            form.save()
            msg="Successfully Registered"
            return render(request,"regsuccess.html",{"msg":msg})
        else:
            return HttpResponse("Registraion Failed")
    return render(request,"Facultyregistration.html",{"form":form})


def interfacelogin(request):
    return render(request,"logininterface.html")






"""def Student(request):
    
    form = StudentForm()
  
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'student_form.html', ) """


"""def Student(request):
    form = StudentForm()
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            msg="Successfully Registered"
            return render(request,"regsuccess.html",{"msg":msg})
        else:
            return HttpResponse("Registraion Failed")
    return render(request,"student_form.html",{'form': form})



def Subject(request):
    form = StudentForm()
    if request.method == "POST":
        form = SubjectForm(request.POST)
        if form.is_valid():
            form.save()
            msg="Successfully Registered"
            return render(request,"regsuccess.html",{"msg":msg})
        else:
            return HttpResponse("Registraion Failed")
    return render(request,"Subject_form.html",{'form': form})


def student_list(request):
    form = Student.objects.all()
    return render(request, 'student_list.html', {'form': form})

def viewsstudents(request):
    usersdata = Student.objects.all()
    userscount = Student.objects.count()

    return render(request,"student_list.html",{"users":usersdata,"count":userscount})


def subject_list(request):
    form = Subject.objects.all()
    return render(request, 'subject_list.html', {'form': form})

def mark_list(request):
    marks = Mark.objects.all()
    return render(request, 'mark_list.html', {'marks': marks})

def mark_create(request):
    if request.method == 'POST':
        form = MarkForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('mark_list'))
    else:
        form = MarkForm()
    return render(request, 'mark_form.html', {'form': form})

def mark_update(request, pk):
    mark = get_object_or_404(Mark, pk=pk)
    if request.method == 'POST':
        form = MarkForm(request.POST, instance=mark)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('mark_list'))
    else:
        form = MarkForm(instance=mark)
    return render(request, 'mark_form.html', {'form': form})

def mark_delete(request, pk):
    mark = get_object_or_404(Mark, pk=pk)
    mark.delete()
    return HttpResponseRedirect(reverse('mark_list'))"""



"""def addsubject(request):
    form = SubjectForm()

    if request.method == "POST":
        form = SubjectForm(request.POST)
        if form.is_valid():
            form.save()
            msg="Subjects Added Successfully"
            return render(request,"add_course.html",{"msg":msg,"subform":form})
        else:
            msg="Failed to Add subjects"
            return render(request, "add_course.html", {"msg": msg,"subform":form})

    return render(request,"add_course.html",{"subform":form})"""

"""def addsubject(request):
    form = addsubjectForm()

    if request.method == "POST":
        form = addsubjectForm(request.POST)

        id = form.data["id"]
        fullname = form.data["fullname"]
       # location = form.data["dept_location"]

        flag = Department.objects.filter(dept_id=id)

        if flag:
            Registration.objects.filter(id=id,name=fullname) #.update(dept_hod=hod, dept_location=location)
            form = SubjectForm()

            if request.method == "POST":
                form = SubjectForm(request.POST)
                if form.is_valid():
                    form.save()
            msg = "Department Updated Successfully"
            return render(request,"add_course.html",{"msg":msg,"subform":form})
        else:
            msg = "Department ID Not Found"
            return render(request,"add_course.html",{"msg":msg,"subform":form})

    else:
        return render(request, "add_course.html", {"subform": form}) """



def addcourse(request):
    form=CourseForm()

    if request.method == "POST":
        form=CourseForm(request.POST)
        if form.is_valid():
            form.save()
            msg="Course Added Successfully"
            return render(request,"add_course.html",{"msg":msg,"courseform":form})
        else:
            msg="Failed to Add course"
            return render(request, "add_course.html", {"msg": msg,"courseform":form})

    return render(request,"add_course.html",{"courseform":form})






'''def viewstudentcourse(request):
    usersdata = Student_Course.objects.all()
    userscount = Student_Course.objects.count()

    course = Course.objects.all()
    return render(request,"userhome.html",{"users":usersdata,"count":userscount,"course":course}) '''




def adminlogin(request):
    return render(request,"adminlogin.html")


def checkadminlogin(request):
    uname = request.POST["ausername"]
    pwd = request.POST["apassword"]

    flag = Admin.objects.filter(Q(username__exact=uname) & Q(password__exact=pwd))
    print(flag)

    if flag:
        admin = Admin.objects.get(username=uname)
        print(admin)
        request.session["auname"] = admin.username
        return render(request, "adminhome.html", {"auname": admin.username})
    else:
        msg = "Login Failed"
        return render(request, "adminlogin.html", {"msg": msg})



'''def facultylogin(request):
    username = request.POST["ausername"]
    pwd = request.POST["apassword"]

    flag = Faculty.objects.filter(Q(username=username) & Q(password=pwd))
    print(flag)

    if flag:
        faculty = Faculty.objects.get(username=username)
        print(faculty)
        request.session["funame"] = faculty.username
        return render(request, "facultyhome.html", {"funame": faculty.f_username})
    else:
        msg = "Login Failed"
        return render(request, "facultylogin.html", {"msg": msg})'''


def checkemplogin(request):
    uname = request.POST["eusername"]
    pwd = request.POST["epassword"]

    flag = Faculty.objects.filter(Q(username=uname) & Q(password=pwd))

    print(flag)

    if flag:
        emp = Faculty.objects.get(username=uname)
        print(emp)
        request.session["eid"] = emp.id
        request.session["ename"] = emp.fullname
        return render(request, "emphome.html", {"eid": emp.id, "ename": emp.fullname,"emp":emp})
    else:
        msg = "Login Failed"
        return render(request, "emplogin.html", {"msg": msg})

def emplogin(request):
    return render(request,"emplogin.html")

def loginpage(request):
    return render(request,"loginpage.html")


def viewfaculty(request):
    usersdata = Faculty.objects.all()
    userscount = Faculty.objects.count()

    return render(request,"viewfaculty.html",{"users":usersdata,"count":userscount})


def viewcourse(request):
    usersdata = Course.objects.all()

    return render(request,"viewcourses.html",{"users":usersdata,})

def studentcourse(request):
    form = CourseForm()
    if request.method == "POST":
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            msg="Successfully Added course"
            return render(request,"regsuccess.html",{"msg":msg})
        else:
            return HttpResponse("Registraion Failed")
    return render(request,"add_course.html",{"form": form,})


"""def viewprofile(request):

    courses = Course.objects.all()
    uname = request.session["uname"]
    student = Student.objects.get(username=uname)
    marks = Marks.objects.filter(student=student)
    print(student)

    return render(request,"viewprofile.html",{"student":student,"courses":courses,"uname":uname,"marks":marks}) """

def viewprofile(request):
    uname = request.session["uname"]
    student = get_object_or_404(Student, username=uname)
    marks = Marks.objects.filter(student=student)
    courses = Course.objects.all()

    context = {
        'student': student,
        'courses': courses,
        'uname': uname,
        'marks': marks,
    }

    return render(request, "viewprofile.html", context)



'''def display(request):
    return render(request,"displayproducts.html")

def updatemarks(request):

    ename = request.session["ename"]

    student = Registration.objects.all()
    count = Registration.objects.count()

    return render(request,"updatemarks.html",{"ename":ename,"student":student,"count":count})


def displaystudents(request):

    eid = request.session["eid"]
    ename = request.session["ename"]

    sname = request.POST["sname"]

    print(sname)

    studentlist = Registration.objects.filter(name__icontains=sname)

    return render(request,"displaystudents.html",{"eid": eid, "ename": ename,"studentlist":studentlist})


def check(request):
    data = Registration.objects.all()
    if 'fullname' in data:
        fullname= data.getlist('fullname')
        print(fullname)

        return HttpResponse("<b> Success</b>")
    else:
        return HttpResponse("<b>failed</b>")


def student_detail(request, pk):
    student = get_object_or_404(Registration, pk=pk)
    marks = Marks.objects.filter(student=student)
    if request.method == 'POST':
        student_form = RegistrationForm(request.POST, instance=student)
        if student_form.is_valid():
            student_form.save()
            return redirect('student_detail', pk=pk)
    else:
        student_form = RegistrationForm(instance=student)
    return render(request, 'student_detail.html', {'student': student, 'marks': marks, 'student_form': student_form})

def mark_edit(request, pk):
    mark = get_object_or_404(Marks, pk=pk)
    if request.method == 'POST':
        mark_form = MarkForm(request.POST, instance=mark)
        if mark_form.is_valid():
            mark_form.save()
            return redirect('student_detail', pk=mark.student.pk)
    else:
        mark_form = MarkForm(instance=mark)
    return render(request, 'mark_update.html', {'mark_form': mark_form})

def mark_create(request):
    form = MarkForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('student-detail')
    context = {
        'form': form,
    }
    return render(request, 'mark_create.html', context) '''



def register_course(request, subject_id):
    studentobj =Student(id=id,course_code=subject_id)
    Student.save(studentobj)
    return HttpResponse("Employee Added Successfully")

    uname = request.session["uname"]

    return render(request, 'registration_success.html', {'subject': course,'uname':uname})


def studentmarks(request):
    form = MarkForm()
    if request.method == "POST":
        form = MarkForm(request.POST)
        if form.is_valid():
            form.save()
            msg="Successfully added marks"
            return render(request,"regsuccess.html",{"msg":msg})
        else:
            return HttpResponse("Registraion Failed")
    return render(request,"add_marks.html",{"form": form,})


def student_list(request):
    students = Student.objects.all()
    context = {'students': students}
    return render(request, 'students_l.html', context)


def enter_marks(request, id):
    student = get_object_or_404(Student, id=id)
    if request.method == 'POST':
        form = MarksForm(request.POST)
        if form.is_valid():
            marks = form.save(commit=False)
            existing_marks = Marks.objects.filter(student=student, subject=marks.subject).exists()
            if existing_marks:
                messages.error(request, 'Marks for this subject already exist. Please edit the existing marks instead.')
            else:
                marks.student = student
                marks.save()
                messages.success(request, 'Marks successfully entered for %s' % student.fullname)
                form = MarksForm()
        else:
            messages.error(request, 'Form is invalid. Please check your input.')
    else:
        form = MarksForm()
    context = {
        'student': student,
        'form': form
    }
    return render(request, 'enter_marks.html', context)









def view_marks(request):
    uname = request.session["uname"]
    student = get_object_or_404(Student, username=uname)
    marks = Marks.objects.filter(student=student)
    courses = Course.objects.all()

    total_marks = 0
    for mark in marks:
        total_marks += mark.marks_obtained



    context = {
        'student': student,
        'courses': courses,
        'uname': uname,
        'marks': marks,
        'total_marks': total_marks,

    }

    return render(request, "viewmarks.html", context)






"""def edit_marks(request, student_id, subject_id):
    student = get_object_or_404(Student, id=student_id)
    subject = get_object_or_404(Course, id=subject_id)
    marks = get_object_or_404(Marks, student=student, subject=subject)
    if request.method == 'POST':
        form = MarksForm(request.POST, instance=marks)
        if form.is_valid():
            form.save()
            messages.success(request, 'Marks successfully updated.')
            return redirect('enter_marks', id=student.id)
        else:
            messages.error(request, 'Form is invalid. Please check your input.')
    else:
        form = MarksForm(instance=marks)
    context = {
        'student': student,
        'subject': subject,
        'form': form,
    }
    return render(request, 'edit_marks.html', context) """

def edit_marks(request, id):
    marks = get_object_or_404(Marks, id=id)
    subject = marks.subject
    student = None
    if request.method == 'POST':
        form = MarksForm(request.POST, instance=marks)
        if form.is_valid():
            form.save()
            messages.success(request, 'Marks successfully updated.')
            return redirect('enter_marks', id=marks.student.id)
        else:
            messages.error(request, 'Form is invalid. Please check your input.')
    else:
        form = MarksForm(instance=marks)
        student = marks.student
    context = {
        'student': student,
        'subject': subject,
        'form': form,
    }
    return render(request, 'edit_marks.html', context)



def leaderboard(request):
    # Get the top 10 students with the highest marks
    top_students = Marks.objects.values('student__username').annotate(total_marks=Sum('marks_obtained')).order_by('-total_marks')[:10]

    # Pass the top students to the template
    context = {'top_students': top_students}
    return render(request, 'leaderboard.html', context)




def student_marks(request):
    students = Student.objects.all()
    labels = [s.username for s in students]
    marks = [s.marks_set.aggregate(total=Sum('marks_obtained'))['total'] or 0 for s in students]

    # Plot the bar chart
    plt.bar(labels, marks)
    plt.xlabel('Students')
    plt.ylabel('Total Marks')
    plt.title('Student Marks')
    plt.show()

    return render(request, 'chart.html')


def newadmin(request):
    return render(request, 'newadminhome.html')


def userleaderboard(request):
    # Get the top 10 students with the highest marks
    top_students = Marks.objects.values('student__username').annotate(total_marks=Sum('marks_obtained')).order_by('-total_marks')[:10]

    # Pass the top students to the template
    context = {'top_students': top_students}
    return render(request, 'userleaderboard.html', context)


def userviewcourse(request):
    usersdata = Course.objects.all()

    return render(request,"userviewcourses.html",{"users":usersdata,})

def empviewusers(request):
    usersdata = Student.objects.all()
    userscount = Student.objects.count()
    return render(request,"empviewusers.html",{"users":usersdata,"count":userscount})

def empleaderboard(request):
    # Get the top 10 students with the highest marks
    top_students = Marks.objects.values('student__username').annotate(total_marks=Sum('marks_obtained')).order_by('-total_marks')[:10]

    # Pass the top students to the template
    context = {'top_students': top_students}
    return render(request, 'empleaderboard.html', context)

def emphome(request):
    return render(request, 'emphome.html')


