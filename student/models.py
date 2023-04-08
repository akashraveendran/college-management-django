from django.db import models

# Create your models here.
from teacher.models import StudentProfile 

class NoticeBoard(models.Model):

    options = (
            ("Poem","Poem"),
            ('Story',"Story"),
            ('Art',"Art"),
            ('Article',"Article"),
            ('Other',"Other"),
        )
    Category = models.CharField(max_length=255,choices=options)
    Title = models.CharField(max_length=255)
    Content = models.CharField(max_length=255)
    Image = models.FileField(upload_to="noticeboard",null=True,blank=True)
    uploaded_date = models.DateField( auto_now=True)
    Status = models.BooleanField(default=False)
    student = models.ForeignKey(StudentProfile,on_delete=models.CASCADE,null=True,blank=True)