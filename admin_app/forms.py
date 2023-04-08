from django.forms import ModelForm
from django.forms import TextInput,Textarea


from .models import NewsAndInfo



class NewsAndInfoForm(ModelForm):
    class Meta:
        model = NewsAndInfo
        fields = ["Category","Title","Content"]
    
        widgets = {
            'Title': TextInput(attrs={"class":"form-control","placeholder":"Enter Title of your work"}),
            'Content': Textarea(attrs={"class":"form-control","placeholder":"Enter Content/Description"}),
        }