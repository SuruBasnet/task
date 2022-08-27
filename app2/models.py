from django.db import models

# Create your models here.


class Section(models.Model):
    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name


class Teacher(models.Model):
    name = models.CharField(max_length=100)
    contact = models.BigIntegerField(default=9876543210)

    def __str__(self):
        return self.name


class Class(models.Model):
    level = models.IntegerField()
    section = models.ForeignKey('Section', on_delete=models.DO_NOTHING)
    teacher = models.ManyToManyField('Teacher')

    def __str__(self):
        return str(self.level)
