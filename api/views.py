from django.shortcuts import render
from rest_framework.views import APIView
from student.models import Student
from teachers.models import Teachers
from classroom.models import Classroom
from classperiod.models import ClassPeriod
from courses.models import Courses


from .serializers import StudentSerializer
from .serializers import TeachersSerializer
from .serializers import ClassroomSerializer
from .serializers import CoursesSerializer
from .serializers import ClassPeriodSerializer
from rest_framework.response import Response

# Create your views here.

class StudentListView (APIView):
    def get(self,request):
        student = Student.object.all()
        serializer = StudentSerializer(student, many = True)
        return Response(serializer.data)

class TeachersListView (APIView):
    def get(self,request):
        teachers = Teachers.object.all()
        serializer = TeachersSerializer(teachers, many = True)
        return Response(serializer.data)


class ClassPeriodListView (APIView):
    def get(self,request):
        classperiod = ClassPeriod.object.all()
        serializer = ClassPeriodSerializer(classperiod, many = True)
        return Response(serializer.data)
    

class ClassroomListView (APIView):
    def get(self,request):
        classroom = Classroom.object.all()
        serializer = ClassroomSerializer(classroom, many = True)
        return Response(serializer.data)


class CoursesListView (APIView):
    def get(self,request):
        course = Courses.object.all()
        serializer = CoursesSerializer(course, many = True)
        return Response(serializer.data)
                        