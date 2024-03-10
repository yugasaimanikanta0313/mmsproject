from django import forms
from .models import Student, Department, Faculty, Course,  Faculty_Course, Admin, Marks


class DateInput(forms.DateInput):
    input_type = "date"

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = "__all__"    # it will display all the fields in the form except default fields like id and registrationtime
        widgets = {"password":forms.PasswordInput(),"dateofbirth":DateInput()}    # additional features of the fields
        labels = {"gender":"Select Gender","contact":"Contact No","studentimage":"Upload profile pic"}  #using this, we can change label name in the form


class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = "__all__"
        labels = {"dept_id":"Enter ID","dept_name":"Enter Name","dept_location":"Select Location","dept_hod":"Provide HOD"}

class UpdateDepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = "__all__"
        labels = {"dept_id": "Enter ID","dept_location": "Select Location","dept_hod": "Provide HOD"}
        exclude = {"dept_name",}

class FacultyForm(forms.ModelForm):
    class Meta:
        model = Faculty
        fields = "__all__"    # it will display all the fields in the form except default fields like id and registrationtime
        widgets = {"password":forms.PasswordInput(),"f_dateofbirth":DateInput()}    # additional features of the fields
        labels = {"f_dateofbirth":"Enter DOB","f_gender":"Select Gender","f_contact":"Provide Contact No","f_fullname":"Enetr Full Name","f_email":"Enter email","f_username":"Username","f_password":"Password","f_qualification":"Qualification"}  #using this, we can change label name in the form
        #exclude = {"gender"}       #using this, we can hide the fields in the form


"""class MarksForm(forms.ModelForm):
    class Meta:
        model = Studentmarks
        fields = "__all__"
        labels = {"dept_id":"Enter ID","dept_name":"Enter Name","dept_location":"Select Location","dept_hod":"Provide HOD"} """


class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = "__all__"
        labels = {"course_title":"Course Title","course_code":"Course Code","course_credits":"Credits"}

"""class StudentCourseForm(forms.ModelForm):
    class Meta:
        model = Student_Course
        fields = "__all__"
        labels = {"fk": "Student name", "fk2": "Course Name"} """


class FacultyCourseForm(forms.ModelForm):
    class Meta:
        model = Faculty_Course
        fields = "__all__"


class AdminLoginForm(forms.ModelForm):
    class Meta:
        model = Admin
        fields = "__all__"
        widgets = {"password":forms.PasswordInput()}




class MarkForm(forms.ModelForm):
    class Meta:
        model = Marks
        fields = "__all__"




class MarksForm(forms.ModelForm):
    class Meta:
        model = Marks
        fields = ['subject', 'marks_obtained']

    def __init__(self, *args, **kwargs):
        student = kwargs.pop('student', None)
        super().__init__(*args, **kwargs)
        if student:
            self.fields['course'].queryset = student.course_set.all()


