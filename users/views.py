from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login,logout
from .forms import UserAddForm
from django.contrib.auth.models import User,Group

from teacher.forms import TeacherProfileForm,StudentProfileForm
from parent.models import ParentProfile
from teacher.models import TeacherProfile,StudentProfile


from .decorators import not_auth_user


# Create your views here.
@not_auth_user
def Index(request):
    teachers = TeacherProfile.objects.all()
    t_count = teachers.count()
    p_count = ParentProfile.objects.all().count()
    s_count = StudentProfile.objects.all().count()
    return render(request,"index.html",{"teachers":teachers,"t_count":t_count,"p_count":p_count,"s_count":s_count})

def SignIn(request):
    if request.method == "POST":
        username = request.POST['uname']
        password = request.POST['password']
        user1 = authenticate(request, username = username , password = password)
        
        if user1 is not None:
            
            request.session['username'] = username
            request.session['password'] = password
            messages.info(request,'Logged In Successfully')
            login(request, user1)
            return redirect('Index')
        
        else:
            messages.info(request,'Username or Password Incorrect')
            return redirect('SignIn')
    return render(request,"login.html")

def adminSignIn(request):
    if request.method == "POST":
        username = request.POST['uname']
        password = request.POST['password']
        user1 = authenticate(request, username = username , password = password)
        
        if user1 is not None:
            
            request.session['username'] = username
            request.session['password'] = password
            messages.info(request,'Logged In Successfully')
            login(request, user1)
            return redirect('Index')
        
        else:
            messages.info(request,'Username or Password Incorrect')
            return redirect('adminSignIn')
    return render(request,"admin/signin.html")

 
def AddStudent(request):
    form = UserAddForm()
    student_form = StudentProfileForm()
    if request.method == "POST":
        form = UserAddForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get("email")
            if User.objects.filter(username = username).exists():
                messages.info(request,"Username Exists")
                return redirect('AddStudent')
            if User.objects.filter(email = email).exists():
                messages.info(request,"Email Exists")
                return redirect('AddStudent')
            else:
                new_user = form.save()
                
                group = Group.objects.get(name='student')
                new_user.groups.add(group) 
                new_user.save()
                
                student_form = StudentProfileForm(request.POST,request.FILES)
                teacher = student_form.save()
                
                teacher.user = new_user
                teacher.save()
                messages.success(request,"Student Created")
                return redirect('viewDepartmentStudents')
        else:
                messages.success(request,"Couldn't perform  Operation ")
    return render(request,"teacher/add-student.html",{"form":form,"student_form":student_form})
def parentSignup(request):
    form = UserAddForm()
    if request.method == "POST":
        form = UserAddForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get("email")
            if User.objects.filter(username = username).exists():
                messages.info(request,"Username Exists")
                return redirect('parentSignup')
            if User.objects.filter(email = email).exists():
                messages.info(request,"Email Exists")
                return redirect('parentSignup')
            else:
                new_user = form.save()
                
                group = Group.objects.get(name='parent')
                new_user.groups.add(group) 
                new_user.save()
                new_user.is_active = False
                new_user.save()
                
                parent = ParentProfile(Phone_Number=request.POST["Phone_Number"],Address=request.POST["Address"],Department=request.POST["Department"])
                parent.parent = new_user
                parent.save()
                messages.success(request,"Successfully Signed up as parent")
                return redirect('parentSignIn')
        else:
                messages.success(request,"Couldn't perform  Operation ")
    return render(request,"parents/signup.html",{"form":form,})

def parentSignIn(request):
    if request.method == "POST":
        username = request.POST['uname']
        password = request.POST['password']
        user1 = authenticate(request, username = username , password = password)
        
        if user1 is not None:
            
            request.session['username'] = username
            request.session['password'] = password
            messages.info(request,'Logged In Successfully')
            login(request, user1)
            return redirect('Index')
        
        else:
            messages.info(request,'Username or Password Incorrect')
            return redirect('parentSignIn')
    return render(request,"parents/signin.html")

def teacherSignUp(request):
    form = UserAddForm()
    teacher_form = TeacherProfileForm()
    if request.method == "POST":
        form = UserAddForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get("email")
            if User.objects.filter(username = username).exists():
                messages.info(request,"Username Exists")
                return redirect('teacherSignUp')
            if User.objects.filter(email = email).exists():
                messages.info(request,"Email Exists")
                return redirect('teacherSignUp')
            else:
                new_user = form.save()
                new_user.save()
                
                group = Group.objects.get(name='teacher')
                new_user.groups.add(group) 
                new_user.is_active = False
                new_user.save()
                
                teacher_form = TeacherProfileForm(request.POST,request.FILES)
                teacher = teacher_form.save()
                
                teacher.user = new_user
                teacher.save()
                messages.success(request,"Teacher Created")
                return redirect('teacherSignIn')
        else:
                messages.success(request,"Couldn't perform  signup")
    return render(request,"teacher/signup.html",{"form":form,"teacher_form":teacher_form})


def teacherSignIn(request):
    if request.method == "POST":
        username = request.POST['uname']
        password = request.POST['password']
        user1 = authenticate(request, username = username , password = password)
        
        if user1 is not None:
            
            request.session['username'] = username
            request.session['password'] = password
            messages.info(request,'Logged In Successfully')
            login(request, user1)
            return redirect('Index')
        
        else:
            messages.info(request,'Username or Password Incorrect')
            return redirect('teacherSignIn')
    return render(request,"teacher/signin.html")


def SignOut(request):
    logout(request)
    return redirect('Index')

