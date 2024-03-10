from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

# . represents current directory

urlpatterns = [
    path("",views.indexfunction,name="index"),
    path("formdemo",views.formdemofunction,name="formdemo"),
    path("displayformdata",views.displayformdatafunction,name="displayformdata"),
    path("logindemo",views.logindemofunction,name="logindemo"),
    path("checklogindemo",views.checklogindemofunction,name="checklogindemo"),
    path("addemployee",views.addemployeefunction,name="addemployee"),


    path("registration",views.registration,name="registration"),
    path("userlogin",views.userlogin,name="userlogin"),
    path("checkuserlogin",views.checkuserlogin,name="checkuserlogin"),



    path("userhome",views.userhome,name="userhome"),
    path("userlogout",views.userlogout,name="userlogout"),
    path("viewusers",views.viewusers,name="viewusers"),

    path("adddepartment",views.adddepartment,name="adddepartment"),

  #  path("updatedepartment",views.updatdepartment,name="updatedepartment"),

    path("deleteuser/<int:uid>",views.deleteuser,name="deleteuser"),

    path("facultyregistration",views.faculty_registration,name="facultyregistration"),

    path("deletefaculty/<int:uid>",views.deletefaculty,name="deletefaculty"),

    path("logininterface",views.interfacelogin,name="logininterface"),

    path("course",views.addcourse,name="course"),



    path('adminlogin',views.adminlogin,name='adminlogin'),
    path('checkadminlogin',views.checkadminlogin,name="checkadminlogin"),
    path('checkemplogin',views.checkemplogin,name='checkemplogin'),
    path('emplogin',views.emplogin,name="emplogin"),
    path('loginpage',views.loginpage,name='loginpage'),

    path('viewfaculty',views.viewfaculty,name='viewfaculty'),
    path('viewcourse',views.viewcourse,name='viewcourse'),
    path('studentcourse',views.studentcourse,name='studentcourse'),
    path('viewprofile',views.viewprofile,name='viewprofile'),

    path('registercourse', views.register_course, name='register_subject'),
    path('studentmarks', views.studentmarks, name='studentmarks'),

    path('list', views.student_list, name='list'),
    path('enter_marks/<int:id>/', views.enter_marks, name='enter_marks'),
    path('view_marks', views.view_marks, name='view_marks'),
    path('edit_marks/<int:id>/', views.edit_marks, name='edit_marks'),
    path('leaderboard',views.leaderboard,name="leaderboard"),
    path('piechart',views.student_marks,name="piechart"),
    path('newadmin',views.newadmin,name="newadmin"),
    path('userleaderboard',views.userleaderboard,name="userleaderboard"),
    path('usercourses', views.userviewcourse,name="usercourses"),
    path('empusers', views.empviewusers,name="empusers"),
    path('empleaderboard',views.empleaderboard,name="empleaderboard"),
    path('emphome',views.emphome,name="emphome"),


]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

