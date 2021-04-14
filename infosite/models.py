from django.db import models
from datetime import datetime

# Create your models here.
class Stud_data(models.Model):
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    rollno = models.CharField(max_length=20)
    dob = models.DateField()
    email = models.EmailField(max_length = 254,unique=True)
    address = models.CharField(max_length=200)
    marks = models.IntegerField()
    student_photo = models.ImageField(upload_to='photos/')
    def __str__(self):
        return self.rollno
