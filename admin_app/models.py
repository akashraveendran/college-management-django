from django.db import models

# Create your models here.
from teacher.models import StudentProfile 

class NewsAndInfo(models.Model):

    options = (
            ('News',"News"),
            ('Other Informations',"Other Informations"),
        )
    Category = models.CharField(max_length=255,choices=options)
    Title = models.CharField(max_length=255)
    Content = models.CharField(max_length=255)
    uploaded_date = models.DateField( auto_now=True)