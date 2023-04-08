from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login,logout

from django.contrib.auth.models import User,Group

from student.models import NoticeBoard
from .models import StudentProfile,AcademicWork,TeacherProfile,AcademicWorkMark,SemesterResult,TimeTable,Attendance
from .forms import AcademicWorkForm,SemesterResultForm,TimeTableForm,AttendanceForm
from admin_app.models import NewsAndInfo
from parent.models import ParentProfile


def teacherIndex(request):
    teachers = TeacherProfile.objects.all()
    t_count = teachers.count()
    p_count = ParentProfile.objects.all().count()
    s_count = StudentProfile.objects.all().count()
    return render(request,"teacher/index.html",{"teachers":teachers,"t_count":t_count,"p_count":p_count,"s_count":s_count})


def viewDepartmentStudents(request):
    students = StudentProfile.objects.all()
    return render(request,"teacher/view-students.html",{"students":students})

def deleteStudent(request,id):
    student = User.objects.get(id=id)
    student.delete()
    messages.info(request,"Student Deleted")
    return redirect("viewDepartmentStudents")

def viewWorks(request):
    teacher = TeacherProfile.objects.get(user = request.user)
    works = AcademicWork.objects.filter(teacher=teacher)
    return render(request,"teacher/view-works.html",{"works":works})


def addWork(request):

    work_form = AcademicWorkForm()
    if request.method == "POST":
        work_form = AcademicWorkForm(request.POST)
        work = work_form.save()

        teacher = TeacherProfile.objects.get(user = request.user)
        work.teacher = teacher
        work.save()       

        messages.success(request,"Work Created")
        return redirect('viewWorks')
    return render(request,"teacher/add-work.html",{"work_form":work_form})


def deleteWork(request,id):
    
    work = AcademicWork.objects.get(id=id)
    work.delete()
    return redirect("viewWorks")

def viewWorkMark(request,id):
    
    work = AcademicWork.objects.get(id=id)
    students = StudentProfile.objects.filter(Department=work.Department,Semester = work.Semester)
    marks = AcademicWorkMark.objects.filter(work=work)
    return render(request,"teacher/view-work-marks.html",{"students":students,"marks":marks,"work":work})

def addmark(request,id):
    if request.method == "POST":
        work = AcademicWork.objects.get(id=id)
        student = StudentProfile.objects.get(id = request.POST["studentID"])
        mark = request.POST["mark"]
        work_mark = AcademicWorkMark(work=work,student=student,mark=mark)
        work_mark.save()
    return redirect("viewWorkMark",id)

def viewSemResults(request):
    teacher = TeacherProfile.objects.get(user=request.user)
    sem_result_form = SemesterResultForm()
    sem_results = SemesterResult.objects.filter(teacher=teacher)
    return render(request,"teacher/view-sem-results.html",{"sem_result_form":sem_result_form,"sem_results":sem_results})

def deleteSemResult(request,id):
    
    sem_results = SemesterResult.objects.filter(id = id)
    sem_results.delete()
    return redirect("viewSemResults")

def addSemesterResult(request):

    if request.method == "POST":
        sem_result_form = SemesterResultForm(request.POST,request.FILES)
        sem_result = sem_result_form.save()

        teacher = TeacherProfile.objects.get(user = request.user)
        sem_result.teacher = teacher
        sem_result.save()

        messages.success(request,"Semester Result Uploaded")
        return redirect('viewSemResults')


def addTimeTable(request):

    timetable_form = TimeTableForm()
    if request.method == "POST":
        timetable_form = TimeTableForm(request.POST,request.FILES)
        timetable = timetable_form.save()

        teacher = TeacherProfile.objects.get(user = request.user)
        timetable.teacher = teacher
        timetable.save()

        messages.success(request,"Timetable Uploaded")
        return redirect('viewTimeTable')
    
    return render(request,"teacher/add-timetable.html",{"timetable_form":timetable_form})

def viewTimeTable(request):
    teacher = TeacherProfile.objects.get(user=request.user)
    timetables = TimeTable.objects.filter(teacher=teacher)
    return render(request,"teacher/view-timetables.html",{"timetables":timetables})

def deletetable(request,id):
    
    work = TimeTable.objects.get(id=id)
    work.delete()
    return redirect("viewTimeTable")


def viewAttendance(request,s_id):
   
    attendance_form = AttendanceForm()
    student = StudentProfile.objects.get(id=s_id)
    attendances = Attendance.objects.filter(student=student)
    return render(request,"teacher/view-student-attendance.html",{"attendance_form":attendance_form,"student":student,"attendances":attendances})

def addAttendance(request,s_id):

    if request.method == "POST":
        student = StudentProfile.objects.get(id=s_id)

        attendance_form = AttendanceForm(request.POST)
        attendance = attendance_form.save()

        teacher = TeacherProfile.objects.get(user = request.user)
        attendance.teacher = teacher
        attendance.student = student
        attendance.save()

        messages.success(request,"Added Attendance Successfully")
        return redirect('viewAttendance',student.id)


def deleteAttendance(request,id):
    
    attendance = Attendance.objects.get(id=id)
    student =  attendance.student 
    attendance.delete()
    return redirect("viewAttendance",student.id)

def viewNewsAndInfo(request):
    return render(request,"teacher/view-news.html")

def viewEvents(request):
    return render(request,"teacher/view-events.html")


def viewTeacherNoticeBoard(request):
    noticeboard_list = NoticeBoard.objects.all()
    return render(request,"teacher/view-noticeboard.html",{"noticeboard_list":noticeboard_list})


def approveArticle(request,id):
    article = NoticeBoard.objects.get(id=id)
    article.Status  = True
    article.save()
    return redirect("viewTeacherNoticeBoard")

def rejectArticle(request,id):
    article = NoticeBoard.objects.get(id=id)
    article.Status  = False
    article.save()
    return redirect("viewTeacherNoticeBoard")


def viewTeacherNews(request):
    news = NewsAndInfo.objects.all()
    return render(request,"teacher/view-news-info.html",{"news":news})

def viewParents(request):
    teacher = TeacherProfile.objects.get(user=request.user)
    students = StudentProfile.objects.filter(Department = teacher.Department)
    parents = ParentProfile.objects.filter(Department=teacher.Department)
    
    new_parents = parents.filter(student=None)
    new_parent_count = new_parents.count()
    return render(request,"teacher/view-parents.html",{"parents":parents,"new_parents":new_parents,"students":students,"new_parent_count":new_parent_count})

def assignStudentParent(request,p_id):
    
    student = StudentProfile.objects.get(id=request.POST["studentId"])
    parent = ParentProfile.objects.get(id=p_id)
    parent.student = student
    p = parent.parent
    p.is_active = True
    p.save()
    parent.save()
    return redirect("viewParents")

def deleteParent(request,p_id):
    
    parent = User.objects.filter(id=p_id)
    parent.delete()
    return redirect("viewParents")