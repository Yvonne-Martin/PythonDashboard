from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from student.models import Student
from teachers.models import Teachers
from classroom.models import Classroom
from classperiod.models import ClassPeriod
from courses.models import Courses
from .serializers import StudentSerializer
from .serializers import TeacherSerializer
from .serializers import ClassPeriodSerializer
from .serializers import ClassroomSerializer
from .serializers import CourseSerializer
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

class StudentListView (APIView):
    def get(self,request):
        student = Student.object.all()
        serializer = StudentSerializer(student, many = True)
        return Response(serializer.data)
    def post(self,request):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
class StudentDetailView(APIView):
    def get (self,request,id):
        Student = Student.objects.get(id=id)
        serializer = StudentSerializer(Student)
        return Response(serializer.data)
            
class StudentDetailView(APIView):
    def put (self,request,id):
        Student = Student.objects.get(id=id)
        serializer = StudentSerializer(Student,data=request.data)
        if serializer.is_valid():
           serializer.save()
           return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class StudentDetailView(APIView):
    def delete (self,request,id):
        Student = Student.objects.get(id=id)
        Student.delete()
        return Response(status=status.HTTP_202_ACCEPTED)
        

class TeachersListView (APIView):
    def get(self,request):
        teachers = Teachers.object.all()
        serializer = TeacherSerializer(teachers, many = True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer = TeacherSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST) 


class TeacherDetailView(APIView):
    def get (self,request,id):
        Teacher = Teacher.objects.get(id=id)
        serializer = TeacherSerializer(Teachers)
        return Response(serializer.data)
            
class TeacherDetailView(APIView):
    def put (self,request,id):
        Teachers = Teachers.objects.get(id=id)
        serializer = TeacherSerializer(Teachers,data=request.data)
        if serializer.is_valid():
           serializer.save()
           return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class TeacherDetailView(APIView):
    def delete (self,request,id):
        Teachers = Teachers.objects.get(id=id)
        Teachers.delete()
        return Response(status=status.HTTP_202_ACCEPTED)   


class ClassPeriodListView (APIView):
    def get(self,request):
        classperiod = ClassPeriod.object.all()
        serializer = ClassPeriodSerializer(classperiod, many = True)
        return Response(serializer.data)

    def post(self,request):
        serializer = ClassPeriodSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
            


class ClassPeriodDetailView(APIView):
    def get (self,request,id):
        ClassPeriod = ClassPeriod.objects.get(id=id)
        serializer = ClassPeriodSerializer(ClassPeriod)
        return Response(serializer.data)
            
class ClassPeriodDetailView(APIView):
    def put (self,request,id):
        ClassPeriod = ClassPeriod.objects.get(id=id)
        serializer = ClassPeriodSerializer(ClassPeriod,data=request.data)
        if serializer.is_valid():
           serializer.save()
           return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class ClassPeriodDetailView(APIView):
    def delete (self,request,id):
        ClassPeriod = ClassPeriod.objects.get(id=id)
        ClassPeriod.delete()
        return Response(status=status.HTTP_202_ACCEPTED)       

    

class ClassroomListView (APIView):
    def get(self,request):
        classroom = Classroom.object.all()
        serializer = ClassroomSerializer(classroom, many = True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer = ClassroomSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        

class ClassroomDetailView(APIView):
    def get (self,request,id):
        Classroom= Classroom.objects.get(id=id)
        serializer = ClassroomSerializer(Classroom)
        return Response(serializer.data)
            
class ClassroomDetailView(APIView):
    def put (self,request,id):
        Classroom = Classroom.objects.get(id=id)
        serializer = ClassroomSerializer(Classroom,data=request.data)
        if serializer.is_valid():
           serializer.save()
           return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class ClassroomDetailView(APIView):
    def delete (self,request,id):
        Classroom = Classroom.objects.get(id=id)
        Classroom.delete()
        return Response(status=status.HTTP_202_ACCEPTED)  


class CoursesListView (APIView):
    def get(self,request):
        courses = Courses.object.all()
        serializer = CourseSerializer(courses, many = True)
        return Response(serializer.data)

    def post(self,request):
        serializer = CourseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


class CoursesDetailView(APIView):
    def get (self,request,id):
        Courses = Courses.objects.get(id=id)
        serializer = CourseSerializer(Courses)
        return Response(serializer.data)
            
class CoursesDetailView(APIView):
    def put (self,request,id):
        Courses = Courses.objects.get(id=id)
        serializer = CourseSerializer(Courses,data=request.data)
        if serializer.is_valid():
           serializer.save()
           return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class CoursesDetailView(APIView):
    def delete (self,request,id):
        Courses = Courses.objects.get(id=id)
        Courses.delete()
        return Response(status=status.HTTP_202_ACCEPTED)  
                        