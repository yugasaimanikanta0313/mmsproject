from django.contrib import admin

from .models import   Faculty, Course,  Faculty_Course, Admin, Marks, Student

admin.site.register(Student)

admin.site.register(Faculty)
admin.site.register(Course)


admin.site.register(Faculty_Course)
admin.site.register(Admin)

admin.site.register(Marks)
