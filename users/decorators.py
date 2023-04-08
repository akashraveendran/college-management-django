from django.shortcuts import redirect


def not_auth_user(view_func):

    def wrapper_function(request, *args, **kwargs):
        if request.user.groups.exists():
            group = request.user.groups.all()[0].name
            print(group)
            if group == 'admin':
                return redirect("admin_home")
            if group == 'teacher':
                return redirect("teacherIndex")
            if group == 'student':
                return redirect("studentIndex")
            if group == 'parent':
                return redirect("parentIndex")
        else:
                return view_func(request, *args, **kwargs)

    return wrapper_function