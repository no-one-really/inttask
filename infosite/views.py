from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return render(request, 'firstpage.html')

def student_information(request):
    return render(request, 'displayinfo.html')
