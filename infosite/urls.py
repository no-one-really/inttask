from django.urls import path

from . import views

urlpatterns=[
 path("",views.index,name='index'),
 path('<str:roll_no>',views.student_information,name='student_information')
]
