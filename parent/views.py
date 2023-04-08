from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login,logout

from django.contrib.auth.models import User,Group
from teacher.models import  StudentProfile,Attendance,AcademicWork,AcademicWorkMark,SemesterResult,TeacherProfile,TimeTable
from .models import ParentProfile
from student.models import NoticeBoard
from admin_app.models import NewsAndInfo

def parentIndex(request):
    teachers = TeacherProfile.objects.all()
    t_count = teachers.count()
    p_count = ParentProfile.objects.all().count()
    s_count = StudentProfile.objects.all().count()
    return render(request,"parents/index.html",{"teachers":teachers,"t_count":t_count,"p_count":p_count,"s_count":s_count})



def parentViewAttendance(request):
   
    p = ParentProfile.objects.get(parent = request.user)
    student = p.student
    attendances = Attendance.objects.filter(student=student)
    a_count = attendances.count()
    return render(request,"parents/view-student-attendance.html",{"a_count":a_count,"student":student,"attendances":attendances})

def viewStudentMarks(request):
    parent = ParentProfile.objects.get(parent=request.user)
    marks = AcademicWorkMark.objects.filter(student=parent.student)
    return render(request,"parents/view-marks.html",{"marks":marks,"student":parent.student})

def parentViewSemResult(request):
    parent = ParentProfile.objects.get(parent=request.user)
    sem_results = SemesterResult.objects.filter(Semester=parent.student.Semester,Department=parent.student.Department)
    return render(request,"parents/view-sem-results.html",{"sem_results":sem_results})

def parentViewIDCard(request):
    parent = ParentProfile.objects.get(parent=request.user)
    return render(request,"parents/view-id-card.html",{"student":parent.student})

def viewParentNoticeBoard(request):
    noticeboard_list = NoticeBoard.objects.filter(Status=True)
    return render(request,"parents/view-notice-board.html",{"noticeboard_list":noticeboard_list})


def viewParentNews(request):
    news = NewsAndInfo.objects.all()
    return render(request,"parents/view-news-info.html",{"news":news})

def viewDepartmentTeachers(request):
    teachers = TeacherProfile.objects.all()
    return render(request,"parents/view-teachers.html",{"teachers":teachers})