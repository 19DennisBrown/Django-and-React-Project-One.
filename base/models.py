from django.db import models

# Create your models here.


class Student(models.Model):
  name = models.CharField(max_length= 100)
  location = models.CharField(max_length= 100)
  hostel = models.CharField(max_length= 100)
  department = models.CharField(max_length= 100)
  age = models.IntegerField()
  year = models.IntegerField()
  date = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return self.name