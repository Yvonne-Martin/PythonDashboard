from django.db import models

# Create your models here.
class Class(models.Model):
    class_name = models.CharField(max_length=20)
    class_teacher= models.CharField(max_length=20)
    class_size = models.PositiveIntegerField()
    class_capacity= models.PositiveBigIntegerField()
    meetings = models.CharField(max_length=20)
    class_rep = models.CharField(max_length=20)
    enrollment = models.PositiveSmallIntegerField()
    class_goal = models.CharField(max_length=30)
    class_vision = models.CharField(max_length=20)
    class_id = models.PositiveSmallIntegerField()
    



    def __self__(self):
        return f"{self.class_name} {self.class_teacher}"