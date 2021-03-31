from django.db import models

# Create your models here.
class Stud_data(models.Model):
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    rollno = models.CharField(max_length=20)
    email = models.EmailField(max_length = 254)
    address = models.CharField(max_length=200)
    marks = models.IntegerField()
    student_photo = models.ImageField(upload_to='photos/')
    def __str__(self):
        return self.name
