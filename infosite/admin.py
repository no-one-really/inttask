from django.contrib import admin
from .models import Stud_data
# Register your models here.

class stud_informationdisplay(admin.ModelAdmin):
    list_display = ('fname','lname','rollno','email')
    list_filter = ('rollno','fname')
admin.site.register(Stud_data,stud_informationdisplay)
