from django.db import models
from courses.models import Courses

# Create your models here.
class Teachers(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField()
    country = models.CharField(max_length=20)
    date_of_birth = models.DateField()
    id_no = models. PositiveSmallIntegerField()
    course = models.ManyToManyField(Courses, related_name="course")
    gender = models.CharField(max_length=20)
    nationality = models.CharField(max_length=20)
    teacher_contact = models.PositiveBigIntegerField()
    account_number = models.PositiveBigIntegerField()
    years_of_experience = models.ImageField()
    




    def __self__(self):
        return f"{self.first_name}"