from django.shortcuts import render
from .serializer import EmployeeSerializer
from .models import Employee
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from rest_framework import mixins,generics,viewsets
from django.shortcuts import render,get_object_or_404


# Create your views here.
# class Employees(APIView):
#   def get(self,request):
#     employees = Employee.objects.all()
#     serializer = EmployeeSerializer(employees,many=True)
#     return Response(serializer.data,status=status.HTTP_200_OK)
  
#   def post(self,request):
#     try:
#       serializer = EmployeeSerializer(data=request.data)
#       if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data,status=status.HTTP_201_CREATED)
#       return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
#     except Employee.DoesNotExist as e:
#       return Response({"message":e},status=status.HTTP_400_BAD_REQUEST)
    
# class EmployeeDetail(APIView):
  # def get_object(self, pk):
  #   try:
  #     return Employee.objects.get(pk=pk)
  #   except Employee.DoesNotExist:
  #     raise Http404
    
  # def get(self,request,pk):
  #   employee = self.get_object(pk)
  #   serializer = EmployeeSerializer(employee)
  #   return Response(serializer.data,status=status.HTTP_200_OK)
  
  # def put(self,request,pk):
  #   employee = self.get_object(pk=pk)
  #   serializer = EmployeeSerializer(employee, data=request.data)
  #   if serializer.is_valid():
  #     serializer.save()
  #     return Response(serializer.data,status=status.HTTP_200_OK)
  #   return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
  
  # def delete(self,request,pk):
  #   employee = self.get_object(pk=pk)
  #   employee.delete()
  #   return Response(status=status.HTTP_204_NO_CONTENT)

"""

#Mixins
class Employees(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView):
  queryset = Employee.objects.all()
  serializer_class = EmployeeSerializer

  def get(self, request):
    return self.list(request)
  
  def post(self,request):
    return self.create(request)
  
#Mixins
class EmployeeDetail(mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,generics.GenericAPIView):
  queryset = Employee.objects.all()
  serializer_class = EmployeeSerializer

  def get(self,request,pk):
    return self.retrieve(request,pk)

  def put(self,request,pk):
    return self.update(request,pk)
  
  def delete(self,request,pk):
    return self.destroy(request,pk)
"""

"""
# Generics
# class Employees(generics.ListAPIView,generics.CreateAPIView):
#   queryset = Employee.objects.all()
#   serializer_class = EmployeeSerializer
class Employees(generics.ListCreateAPIView):
  queryset = Employee.objects.all()
  serializer_class = EmployeeSerializer

#Generics
# class EmployeeDetail(generics.RetrieveAPIView,generics.UpdateAPIView,generics.DestroyAPIView):
#   queryset = Employee.objects.all()
  # serializer_class = EmployeeSerializer
class EmployeeDetail(generics.RetrieveUpdateDestroyAPIView):
  queryset = Employee.objects.all()
  serializer_class = EmployeeSerializer
  lookup_field = 'pk'
"""
  
"""
class EmployeeViewset(viewsets.ViewSet):
  def list(self,request):
    queryset = Employee.objects.all()
    serializer = EmployeeSerializer(queryset,many=True)
    return Response(serializer.data)
  
  def create(self, request):
    serializer = EmployeeSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data,status=status.HTTP_201_CREATED)
    return Response(serializer.errors)

  def retrieve(self,request,pk=None):
    employee = get_object_or_404(Employee,pk=pk)
    serializer = EmployeeSerializer(employee)
    return Response(serializer.data,status=status.HTTP_200_OK)
  
  def update(self,request,pk=None):
    employee = get_object_or_404(Employee,pk=pk)
    serializer = EmployeeSerializer(employee,data=request.data,)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data,status=status.HTTP_200_OK)
    return Response(serializer.errors,status=status.HTTP_404_NOT_FOUND)
  
  def delete(self,request,pk=None):
    employee = get_object_or_404(Employee,pk=pk)
    employee.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
"""

class EmployeeViewset(viewsets.ModelViewSet):
  queryset = Employee.objects.all()
  serializer_class = EmployeeSerializer
