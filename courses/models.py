from django.db import models


# Create your models here.
class Courses(models.Model):
    course_name = models.CharField(max_length=20)
    course_teacher= models.CharField(max_length=20)
    course_duration = models.TimeField()
    course_level= models.PositiveSmallIntegerField()
    course_resources = models.CharField(max_length=50)
    course_description = models.CharField(max_length=50)
    course_title = models.CharField(max_length=40)
    course_objectives = models.CharField(max_length=20)
    course_choices = models.CharField(max_length=20, choices = [{"Active","Active"},("Inactive","Inactive")])
    course_id = models.PositiveSmallIntegerField()
    



    def __self__(self):
        return f"{self.course_name} {self.course_id}"