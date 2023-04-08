from django.urls import path 
from .import views

urlpatterns = [
    path("",views.studentIndex,name="studentIndex"),
    path("viewStudentWorks",views.viewStudentWorks,name="viewStudentWorks"),
    path("viewStudentWorkMark/<int:id>",views.viewStudentWorkMark,name="viewStudentWorkMark"),
    path("viewStudentIdCard",views.viewStudentIdCard,name="viewStudentIdCard"),
    path("viewStudentSemResults",views.viewStudentSemResults,name="viewStudentSemResults"),
    path("viewStudentTimeTable",views.viewStudentTimeTable,name="viewStudentTimeTable"),
    path("viewNoticeBoard",views.viewNoticeBoard,name="viewNoticeBoard"),
    path("addNewNotice",views.addNewNotice,name="addNewNotice"),
    path("viewStudentNews",views.viewStudentNews,name="viewStudentNews"),
    path("viewStudentAttendance",views.viewStudentAttendance,name="viewStudentAttendance"),
]