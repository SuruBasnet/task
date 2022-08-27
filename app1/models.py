from django.db import models

# Create your models here.


class Subject(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    subject = models.ManyToManyField('subject')
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.name
