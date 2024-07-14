from django.db import models
# from .models import Teachers

# Create your models here.
class Class(models.Model):
    class_name = models.CharField(max_length=20)
    # teacher= models.ManyToManyField(Teachers, onDelete = models.CASCADE)
    class_size = models.PositiveIntegerField()
    class_capacity= models.PositiveBigIntegerField()
    meetings = models.DateField()
    class_rep = models.CharField(max_length=20)
    enrollment = models.PositiveSmallIntegerField()
    class_goal = models.TextField()
    class_vision = models.TextField()
    class_id = models.PositiveSmallIntegerField()
    
    
    



    def __self__(self):
        return f"{self.class_name} {self.class_teacher}"