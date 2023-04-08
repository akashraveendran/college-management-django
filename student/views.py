from django.shortcuts import render,redirect
from django.contrib import messages


from teacher.models import TeacherProfile,AcademicWork,StudentProfile,AcademicWorkMark,SemesterResult,TimeTable,Attendance

from .forms import NoticeBoardForm
from .models import NoticeBoard
from admin_app.models import  NewsAndInfo
from parent.models import ParentProfile


def studentIndex(request):
    teachers = TeacherProfile.objects.all()
    t_count = teachers.count()
    p_count = ParentProfile.objects.all().count()
    s_count = StudentProfile.objects.all().count()
    return render(request,"student/index.html",{"teachers":teachers,"t_count":t_count,"p_count":p_count,"s_count":s_count})


def viewStudentWorks(request):
    student = StudentProfile.objects.get(user = request.user)
    works = AcademicWork.objects.filter(Department=student.Department,Semester=student.Semester)
    return render(request,"student/view-works.html",{"works":works})

def viewStudentWorkMark(request,id):
    work = AcademicWork.objects.get(id=id)
    marks = AcademicWorkMark.objects.filter(work=work)
    return render(request,"student/view-marks.html",{"marks":marks,"work":work})


def viewStudentIdCard(request):
    student = StudentProfile.objects.get(user = request.user)
    return render(request,"student/view-id-card.html",{"student":student})


def viewStudentSemResults(request):
    student = StudentProfile.objects.get(user=request.user)
    sem_results = SemesterResult.objects.filter(Semester=student.Semester,Department=student.Department)
    return render(request,"student/view-sem-results.html",{"sem_results":sem_results})



def viewStudentTimeTable(request):
    student = StudentProfile.objects.get(user=request.user)
    timetables = TimeTable.objects.filter(Semester=student.Semester,Department=student.Department)
    return render(request,"student/view-timetable.html",{"timetables":timetables})

def viewNoticeBoard(request):
    student = StudentProfile.objects.get(user=request.user)
    noticeboard_list = NoticeBoard.objects.filter(Status=True)

    return render(request,"student/view-notice-board.html",{"noticeboard_list":noticeboard_list,"student":student})

def addNewNotice(request):
    notice_form = NoticeBoardForm()
    if request.method == "POST":
        notice_form = NoticeBoardForm(request.POST,request.FILES)
        noticeboard = notice_form.save()

        student = StudentProfile.objects.get(user = request.user)
        noticeboard.student = student
        noticeboard.save()

        messages.success(request,"Article Uploaded. Please Wait for Teachers Approval")
        return redirect('viewNoticeBoard')
    return render(request,"student/upload-to-noticeboard.html",{"notice_form":notice_form})


def viewStudentNews(request):
    news = NewsAndInfo.objects.all()
    return render(request,"student/view-news-info.html",{"news":news})


def viewStudentAttendance(request):
   
    student = StudentProfile.objects.get(user=request.user)
    attendances = Attendance.objects.filter(student=student)
    a_count = attendances.count()
    return render(request,"student/view-student-attendance.html",{"a_count":a_count,"student":student,"attendances":attendances})
