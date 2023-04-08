from django.urls import path 
from .import views

urlpatterns = [
    path("",views.admin_home,name="admin_home"),
    path("viewTeachers",views.viewTeachers,name="viewTeachers"),
    path("approveTeacher/<int:t_id>",views.approveTeacher,name="approveTeacher"),
    path("viewAddedNews",views.viewAddedNews,name="viewAddedNews"),
    path("addNews",views.addNews,name="addNews"),
    path("removeNews/<int:id>",views.removeNews,name="removeNews"),
    path("viewStudents",views.viewStudents,name="viewStudents"),
    path("removeStudent/<int:id>",views.removeStudent,name="removeStudent"),
    path("viewAllParents",views.viewAllParents,name="viewAllParents"),
    path("adminRemoveParent/<int:id>",views.adminRemoveParent,name="adminRemoveParent"),
]