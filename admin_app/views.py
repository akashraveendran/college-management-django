from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login,logout

from django.contrib.auth.models import User,Group

from teacher.models import TeacherProfile,StudentProfile
from django.contrib.auth.models import User

from .forms import NewsAndInfoForm
from .models import NewsAndInfo
from parent.models import ParentProfile



def admin_home(request):
    teachers = TeacherProfile.objects.all()
    t_count = teachers.count()
    p_count = ParentProfile.objects.all().count()
    s_count = StudentProfile.objects.all().count()
    return render(request,"admin/index.html",{"teachers":teachers,"t_count":t_count,"p_count":p_count,"s_count":s_count})

def viewTeachers(request):
    teachers = TeacherProfile.objects.all()
    return render(request,"admin/view-teachers.html",{"teachers":teachers})

def viewStudents(request):
    students = StudentProfile.objects.all()
    return render(request,"admin/view-students.html",{"students":students})

def viewAllParents(request):
    parents = ParentProfile.objects.all()
    return render(request,"admin/view-parents.html",{"parents":parents})

def approveTeacher(request,t_id):
    teacher = User.objects.get(id = t_id)
    teacher.is_active = True
    teacher.save()
    messages.success(request,"Approved Teacher")
    return redirect("viewTeachers")


def viewAddedNews(request):
    news = NewsAndInfo.objects.all()
    return render(request,"admin/view-news-info.html",{"news":news})

def addNews(request):
    news_form  = NewsAndInfoForm()
    if request.method == "POST":
        news_form = NewsAndInfoForm(request.POST,request.FILES)
        news = news_form.save()
        news.save()

        messages.success(request," News/informations Uploaded")
        return redirect('viewAddedNews')
    return render(request,"admin/add-news-info.html",{"news_form":news_form})


def removeNews(request,id):
    news = NewsAndInfo.objects.get(id=id)
    news.delete()
    return redirect("viewAddedNews")

def removeStudent(request,id):
    news = User.objects.get(id=id)
    news.delete()
    return redirect("viewStudents")

def adminRemoveParent(request,id):
    news = User.objects.get(id=id)
    news.delete()
    return redirect("viewAllParents")