from django.forms import ModelForm
from django.forms import TextInput,Textarea,NumberInput,DateInput
from .models import TeacherProfile,StudentProfile,AcademicWork,SemesterResult,TimeTable,Attendance

class TeacherProfileForm(ModelForm):
    class Meta:
        model = TeacherProfile
        fields = ["Address","Qualification","Phone_Number","Designation","Department","Profile_Image"]

        widgets = {
            'Phone_Number': TextInput(attrs={"class":"form-control","placeholder":"Enter Phone number"}),
            'Designation': TextInput(attrs={"class":"form-control","placeholder":"Enter  Your Designation"}),
            'Address': Textarea(attrs={"class":"form-control","placeholder":"Enter  Address"}),
            'Qualification': Textarea(attrs={"class":"form-control","placeholder":"Enter  Your Educational Qualification"}),
        }


class StudentProfileForm(ModelForm):
    class Meta:
        model = StudentProfile
        fields = ["Register_Number","Phone_Number","Department","Semester","Date_of_birth","Blood_Group","Address","Profile_Image"]

        widgets = {
            'Phone_Number': TextInput(attrs={"class":"form-control","placeholder":"Enter Phone number"}),
            'Date_of_birth':DateInput(attrs={"class":"form-control",'type':"date"}),
            'Address': Textarea(attrs={"class":"form-control","placeholder":"Enter  Address"}),
            'Blood_Group': TextInput(attrs={"class":"form-control","placeholder":"Enter  Blood Group"}),
            'Register_Number': NumberInput(attrs={"class":"form-control","placeholder":"Enter Your Register Number"}),
        }


class AcademicWorkForm(ModelForm):
    class Meta:
        model = AcademicWork
        fields = ["work_title","work_type","Department","Semester","total_mark","Date_of_Submission"]

        widgets = {
            'Date_of_Submission':DateInput(attrs={"class":"form-control",'type':"date"}),
            'work_title': TextInput(attrs={"class":"form-control","placeholder":"Enter Work Title"}),
            'total_mark': NumberInput(attrs={"class":"form-control","placeholder":"Enter Total Marks"}),
        }


class SemesterResultForm(ModelForm):
    class Meta:
        model = SemesterResult
        fields = ["Department","Semester","Semester_Result"]


class TimeTableForm(ModelForm):
    class Meta:
        model = TimeTable
        fields = ["Department","Semester","timetable","Description"]
    
        widgets = {
            'Description': TextInput(attrs={"class":"form-control","placeholder":"Enter Description"}),
        }


class AttendanceForm(ModelForm):
    class Meta:
        model = Attendance
        fields = ["attendance","Attendance_Date"]
    
        widgets = {
            'Attendance_Date': TextInput(attrs={"class":"form-control","type":"date"}),
        }