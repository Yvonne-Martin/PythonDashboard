from django.db import models

# Create your models here.
class Teachers(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField()
    country = models.CharField(max_length=20)
    date_of_birth = models.DateField()
    id_no = models. PositiveSmallIntegerField()
    course = models.CharField(max_length=20)
    gender = models.CharField(max_length=20)
    place_of_birth = models.CharField(max_length=20)
    nationality = models.CharField(max_length=20)



    def __self__(self):
        return f"{self.first_name} {self.id}"