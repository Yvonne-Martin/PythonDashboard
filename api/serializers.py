from rest_framework import serializers
from student.models import Student
from teachers.models import Teachers
from courses.models import Courses
from classroom.models import Classroom
from classperiod.models import ClassPeriod


class StudentSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Student
        fields = "__all__"

                
    class CoursesSerializer(serializers.ModelSerializer):
        class Meta:
            model = Courses
            fields = "__all__"
    

    class TeachersSerializer(serializers.ModelSerializer):
        class Meta:
            model = Teachers
            fields = "__all__"


    class ClassroomSerializer(serializers.ModelSerializer):
        class Meta:
            model = Classroom
            fields = "__all__"

    
    class ClassPeriodSerializer(serializers.ModelSerializer):
        class Meta:
            model = ClassPeriod
            fields = "__all__"        