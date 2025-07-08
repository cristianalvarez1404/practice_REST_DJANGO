from django.contrib import admin
from django.urls import path
from . import views
from employees.views import Employees,EmployeeDetail

urlpatterns = [
  path('students/', views.studentsView ),
  path('students/<int:pk>/',views.studentDetailView),
  path('employees/', Employees.as_view()),
  path('employees/<int:pk>/', EmployeeDetail.as_view())
]