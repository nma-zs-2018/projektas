from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100)
    section = models.CharField(max_length=100)
    image = models.ImageField(upload_to='student', blank=True, null=True)

    def __str__(self):
        return self.name

class Question(models.Model):
    question = models.CharField(max_length=100)
    answer = models.CharField(max_length=100)

    def __str__(self):
        return self.question