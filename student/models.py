from django.db import models
from courses.models import Courses

# Create your models here.

class Student(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField()
    country = models.CharField(max_length=20)
    date_of_birth = models.DateField()
    codehive_id = models. PositiveSmallIntegerField()
    student_guardian = models.CharField(max_length=20)
    course = models.ManyToManyField(Courses, related_name="courses")


    def __self__(self):
        return f"{self.first_name} {self.last_name}"




