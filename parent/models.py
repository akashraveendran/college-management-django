from django.db import models
from django.contrib.auth.models import User

from teacher.models import StudentProfile

class ParentProfile(models.Model):
    
    Phone_Number = models.IntegerField()
    Address = models.CharField(max_length=255)
    Department = models.CharField(max_length=255,null=True,blank=True)
    student = models.ForeignKey(StudentProfile,on_delete=models.CASCADE,null=True,blank=True)
    parent = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)