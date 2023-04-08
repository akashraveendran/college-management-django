from django.urls import path 
from .import views

urlpatterns = [
    path("",views.parentIndex,name="parentIndex"),
    path("parentViewAttendance",views.parentViewAttendance,name="parentViewAttendance"),
    path("viewStudentMarks",views.viewStudentMarks,name="viewStudentMarks"),
    path("parentViewSemResult",views.parentViewSemResult,name="parentViewSemResult"),
    path("parentViewIDCard",views.parentViewIDCard,name="parentViewIDCard"),
    path("viewParentNoticeBoard",views.viewParentNoticeBoard,name="viewParentNoticeBoard"),
    path("viewParentNews",views.viewParentNews,name="viewParentNews"),
    path("viewDepartmentTeachers",views.viewDepartmentTeachers,name="viewDepartmentTeachers"),
]