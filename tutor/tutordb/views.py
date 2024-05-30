from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets
from .models import Student
from .serializers import StudentSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET'])
def get_student(request, student_id):
    try:
        student = Student.objects.get(id=student_id)
    except Student.DoesNotExist:
        return Response(status=404)

    serializer = StudentSerializer(student)
    return Response(serializer.data)
