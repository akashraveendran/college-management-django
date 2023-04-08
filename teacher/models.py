from django.db import models
from django.contrib.auth.models import User


class TeacherProfile(models.Model):
    options = (
    ("Computer Science Engineerning","Computer Science Engineerning"),
    ("Electronics Engineerning","Electronics Engineerning"),
    ("Civil Engineerning","Civil Engineerning"),
    ("Mechanical Engineerning","Mechanical Engineerning"),
    ("Electrical Engineerning","Electrical Engineerning")
    )
    Department = models.CharField(max_length=255,choices=options)
    Phone_Number = models.IntegerField()
    Address = models.CharField(max_length=255)
    Qualification = models.CharField(max_length=255)
    Designation = models.CharField(max_length=255)
    Profile_Image = models.FileField(upload_to="teachers")
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)

class StudentProfile(models.Model):
    options = (
    ("Computer Science Engineerning","Computer Science Engineerning"),
    ("Electronics Engineerning","Electronics Engineerning"),
    ("Civil Engineerning","Civil Engineerning"),
    ("Mechanical Engineerning","Mechanical Engineerning"),
    ("Electrical Engineerning","Electrical Engineerning")
    )
    sems = (
        ("semester 1","semester 1"),
        ("semester 2","semester 2"),
        ("semester 3","semester 3"),
        ("semester 4","semester 4"),
        ("semester 5","semester 5"),
        ("semester 6","semester 6"),
    )
    Semester = models.CharField(max_length=255,choices=sems)
    Department = models.CharField(max_length=255,choices=options)
    Register_Number = models.CharField(max_length=255)
    Blood_Group = models.CharField(max_length=255,null=True,blank=True)
    Date_of_birth = models.DateField(blank=True)
    Phone_Number = models.IntegerField()
    Address = models.CharField(max_length=255)
    Profile_Image = models.FileField(upload_to="students")
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    

class Attendance(models.Model):
        options = (
            ("Full Day","Full Day"),
            ('Half Day',"Half Day"),
            ('Late',"Late"),
            ('Absent',"Absent"),
        )
        attendance = models.CharField(max_length=255,choices=options)
        Attendance_Date = models.DateField()
        student = models.ForeignKey(StudentProfile,on_delete=models.CASCADE,null=True,blank=True)
        date_taken = models.DateField( auto_now=True)
        teacher = models.ForeignKey(TeacherProfile,on_delete=models.CASCADE,null=True,blank=True)



class AcademicWork(models.Model):

    options = (
    ("Computer Science Engineerning","Computer Science Engineerning"),
    ("Electronics Engineerning","Electronics Engineerning"),
    ("Civil Engineerning","Civil Engineerning"),
    ("Mechanical Engineerning","Mechanical Engineerning"),
    ("Electrical Engineerning","Electrical Engineerning")
    )
    sems = (
        ("semester 1","semester 1"),
        ("semester 2","semester 2"),
        ("semester 3","semester 3"),
        ("semester 4","semester 4"),
        ("semester 5","semester 5"),
        ("semester 6","semester 6"),
    )
    work = (
        ("Series Test","Series Test"),
        ('Assignement',"Assignement"),
        ('Project',"Project"),
    )
    Semester = models.CharField(max_length=255,choices=sems)
    Department = models.CharField(max_length=255,choices=options)
    work_type = models.CharField(max_length=255,choices=work)
    work_title = models.CharField(max_length=255)
    total_mark = models.IntegerField(blank=True,null=True)
    Date_assigned = models.DateField(auto_now=True)
    Date_of_Submission = models.DateField()
    teacher = models.ForeignKey(TeacherProfile,on_delete=models.CASCADE,null=True,blank=True)
  

class AcademicWorkMark(models.Model):

    work =  models.ForeignKey(AcademicWork,on_delete=models.CASCADE,null=True,blank=True)
    mark = models.IntegerField()
    student = models.ForeignKey(StudentProfile,on_delete=models.CASCADE,null=True,blank=True)

 
class TimeTable(models.Model):
    options = (
    ("Computer Science Engineerning","Computer Science Engineerning"),
    ("Electronics Engineerning","Electronics Engineerning"),
    ("Civil Engineerning","Civil Engineerning"),
    ("Mechanical Engineerning","Mechanical Engineerning"),
    ("Electrical Engineerning","Electrical Engineerning")
    )
    sems = (
        ("semester 1","semester 1"),
        ("semester 2","semester 2"),
        ("semester 3","semester 3"),
        ("semester 4","semester 4"),
        ("semester 5","semester 5"),
        ("semester 6","semester 6"),
    )
    Semester = models.CharField(max_length=255,choices=sems)
    Department = models.CharField(max_length=255,choices=options)
    Date_assigned = models.DateField(auto_now=True)
    Description = models.CharField(max_length=255,blank=True,null=True)
    timetable = models.FileField(upload_to="timetable")
    teacher = models.ForeignKey(TeacherProfile,on_delete=models.CASCADE,null=True,blank=True)

class SemesterResult(models.Model):
    options = (
    ("Computer Science Engineerning","Computer Science Engineerning"),
    ("Electronics Engineerning","Electronics Engineerning"),
    ("Civil Engineerning","Civil Engineerning"),
    ("Mechanical Engineerning","Mechanical Engineerning"),
    ("Electrical Engineerning","Electrical Engineerning")
    )
    sems = (
        ("semester 1","semester 1"),
        ("semester 2","semester 2"),
        ("semester 3","semester 3"),
        ("semester 4","semester 4"),
        ("semester 5","semester 5"),
        ("semester 6","semester 6"),
    )
    Semester = models.CharField(max_length=255,choices=sems)
    Department = models.CharField(max_length=255,choices=options)
    Semester_Result = models.FileField(upload_to="semresult")
    Date_assigned = models.DateField(auto_now=True)
    teacher = models.ForeignKey(TeacherProfile,on_delete=models.CASCADE,null=True,blank=True)