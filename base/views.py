
from .models import Student
from .serializers import StudentSerializer
from django.shortcuts import render, redirect
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view


@api_view(['GET','POST'])
def Students_view(request):
  if request.method == 'GET':
    students = Student.objects.all()
    serializers = StudentSerializer(students, many=True)
    return Response(serializers.data)
  
  if request.method == 'POST':
    serializers = StudentSerializer(data = request.data)
    if serializers.is_valid():
      serializers.save()
      return Response(serializers.data, status=status.HTTP_201_CREATED)
    
@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def Student_view(request, id):

  try:
    student = Student.objects.get(id=id)
  except:
    return Response(status=status.HTTP_404_NOT_FOUND)

  if request.method == 'GET':
    serializer = StudentSerializer(student)
    return Response(serializer.data)
  
  elif request.method == 'PUT':
    serializer = StudentSerializer(student, data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)
    else:
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  
  elif request.method == 'DELETE':
    student.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
