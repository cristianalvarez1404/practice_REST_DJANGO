from django.contrib import admin
from django.urls import path,include
from . import views
# from employees.views import Employees,EmployeeDetail,EmployeeViewset
from employees.views import EmployeeViewset
from rest_framework.routers import DefaultRouter
from blogs.views  import BlogsView,CommentsView

# urlpatterns = [
#   path('students/', views.studentsView ),
#   path('students/<int:pk>/',views.studentDetailView),
  
#   path('employees/', Employees.as_view()),
#   path('employees/<int:pk>/', EmployeeDetail.as_view())
# ]

#Working with viewset we neet to router

router = DefaultRouter()
router.register('employees', EmployeeViewset,basename='employee')

urlpatterns = [
  path('students/', views.studentsView ),
  path('students/<int:pk>/',views.studentDetailView),

  path('',include(router.urls)),
  path('blogs/', BlogsView.as_view()),
  path('comments/', CommentsView.as_view()),
]