from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from django.forms import ModelForm
from django.forms import TextInput,PasswordInput




class UserAddForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["first_name","email","username","password1","password2"]
        widgets = {
            'username': TextInput(attrs={"class":"form-control","placeholder":"Enter Username"}),
            'first_name': TextInput(attrs={"class":"form-control","placeholder":"Enter Your Name"}),
            'email': TextInput(attrs={"class":"form-control","placeholder":"Enter  Email Address"}),
        }
    def __init__(self, *args, **kwargs) :
        super().__init__(*args, **kwargs)
        self.fields["password1"].widget.attrs.update({"class":"form-control","placeholder":"Enter Password "})
        self.fields["password2"].widget.attrs.update({"class":"form-control","placeholder":"Confirm Password "})
        
