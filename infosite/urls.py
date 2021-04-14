from django.urls import path,re_path

from . import views

urlpatterns=[
 path("",views.index,name='index'),
 re_path(r'[0-9]+[A-Z]+[0-9]*',views.student_information,name='student_information'),
 path('login',views.login,name='login'),
 path('logout',views.logout,name='logout'),
 # path('unsuccessful',views.unsuccessful,name='unsuccessful'),
]
