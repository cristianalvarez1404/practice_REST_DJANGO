from django.shortcuts import render
from django.http import JsonResponse
from students.models import Student
from .serializers import StudentSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status


@api_view(['GET','POST'])
def studentsView(request):
  if request.method == "GET":
    #Get all data from students
    students = Student.objects.all()
    serializer = StudentSerializer(students,many=True)
    return Response(serializer.data,status=status.HTTP_200_OK)
  
  elif request.method == "POST":
    serializer = StudentSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data,status=status.HTTP_201_CREATED)
    
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST )
  
@api_view(["GET","PUT","DELETE"])
def studentDetailView(request,pk):
  try:
    student = Student.objects.get(id=pk)
  except Student.DoesNotExist:
      return Response({"message":"Student does not exist"},status=status.HTTP_404_NOT_FOUND)
    
  if request.method == "GET":
    serializer = StudentSerializer(student)
    return Response(serializer.data,status=status.HTTP_200_OK)
    
  elif request.method == "PUT":
    serializer = StudentSerializer(student,data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data,status=status.HTTP_200_OK)
    else:
      return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
  
  elif request.method == "DELETE":
    student.delete()
    return Response({"message":"User deleted sucessfully"},status=status.HTTP_204_NO_CONTENT)
