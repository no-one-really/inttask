from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from django.shortcuts import redirect
from .models import Stud_data
# Create your views here.

def index(request):
    return render(request, 'firstpage.html')

def logout(request):
    return render(request, 'firstpage.html')

def login(request):
    print('submitted reg')
    roll_number= request.POST['rollnumber']
    password_given=request.POST['pwd']
    print(roll_number)
    data= Stud_data
    uiop='/'+roll_number
    if isinstance(roll_number[0],int):
        return redirect(uiop,roll_number)
    else:
        submition_check={
                         'unsuccessful_submit': True,
                         }
        print(submition_check['unsuccessful_submit'])
        return render(request, 'firstpage.html',submition_check)


def student_information(request):
    rollop=request.path
    rollop=rollop[1:]
    try:
        to_disp = Stud_data.objects.get(rollno=rollop)

        print(to_disp.fname)
        disp_data = {
        'to_disp': to_disp
        }
        print("clear ")

        return render(request, 'profile.html', disp_data)


    except:
        submition_check={
                         'unsuccessful_submit': True,
                         }
        print(submition_check['unsuccessful_submit'])
        return render(request, 'firstpage.html',submition_check)
