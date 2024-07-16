from django.db import models


# Create your models here.
class Classroom(models.Model):
    class_name = models.CharField(max_length=20)
    class_size = models.PositiveIntegerField()
    class_capacity= models.PositiveBigIntegerField()
    meetings = models.DateField()
    class_rep = models.CharField(max_length=20)
    enrollment = models.PositiveSmallIntegerField()
    class_goal = models.TextField()
    class_vision = models.TextField()
    class_id = models.PositiveSmallIntegerField()
    
    
    



    def __self__(self):
        return f"{self.class_name} {self.teacher}"