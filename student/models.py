from django.db import models
# from .models import Course

# Create your models here.

class Student(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField()
    country = models.CharField(max_length=20)
    date_of_birth = models.DateField()
    codehive_id = models. PositiveSmallIntegerField()
    student_guardian = models.CharField(max_length=20)
    # course = models.ManyToManyField(Course, onDelete=models.CASCADE)


    def __self__(self):
        return f"{self.first_name} {self.last_name}"




