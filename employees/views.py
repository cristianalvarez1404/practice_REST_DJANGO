from django.shortcuts import render
from .serializer import EmployeeSerializer
from .models import Employee
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404

# Create your views here.
class Employees(APIView):
  def get(self,request):
    employees = Employee.objects.all()
    serializer = EmployeeSerializer(employees,many=True)
    return Response(serializer.data,status=status.HTTP_200_OK)
  
  def post(self,request):
    try:
      serializer = EmployeeSerializer(data=request.data)
      if serializer.is_valid():
        serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)
      return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    except Employee.DoesNotExist as e:
      return Response({"message":e},status=status.HTTP_400_BAD_REQUEST)
    
class EmployeeDetail(APIView):
  def get_object(self, pk):
    try:
      return Employee.objects.get(pk=pk)
    except Employee.DoesNotExist:
      raise Http404
    
  def get(self,request,pk):
    employee = self.get_object(pk)
    serializer = EmployeeSerializer(employee)
    return Response(serializer.data,status=status.HTTP_200_OK)