from django.db import models

class Students(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField()
    enrollment_date = models.DateField()
class Course(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    students = models.ManyToManyField(Students, related_name='courses')
    start_date = models.DateField()
    end_date = models.DateField()