from django.urls import path 
from .import views

urlpatterns = [
    path("",views.Index,name="Index"),
    path("SignIn",views.SignIn,name="SignIn"),
    path("SignOut",views.SignOut,name="SignOut"),
    path("adminSignIn",views.adminSignIn,name="adminSignIn"),
    path("teacherSignUp",views.teacherSignUp,name="teacherSignUp"),
    path("teacherSignIn",views.teacherSignIn,name="teacherSignIn"),
    path("AddStudent",views.AddStudent,name="AddStudent"),
    path("parentSignup",views.parentSignup,name="parentSignup"),
    path("parentSignIn",views.parentSignIn,name="parentSignIn"),
]