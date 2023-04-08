from django.forms import ModelForm
from django.forms import TextInput,Textarea,NumberInput,DateInput


from .models import NoticeBoard



class NoticeBoardForm(ModelForm):
    class Meta:
        model = NoticeBoard
        fields = ["Category","Title","Content","Image"]
    
        widgets = {
            'Title': TextInput(attrs={"class":"form-control","placeholder":"Enter Title of your work"}),
            'Content': Textarea(attrs={"class":"form-control","placeholder":"Enter Content/Description"}),
        }