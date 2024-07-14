from django.shortcuts import render
from rest_framework.views import APIView
from student.models import Student
from .serializers import StudentSerializer
from rest_framework.response import Response

# Create your views here.

class StudentListView (APIView):
    def get(self,request):
        student = Student.object.all()
        serializer = StudentSerializer(student, many = True)
        return Response(serializer.data)
        