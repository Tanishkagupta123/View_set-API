from django.db import models
from django.core.validators import MaxLengthValidator,MinLengthValidator
from django.core.exceptions import ValidationError

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    contact = models.CharField()
    gender = models.CharField(max_length=10)
    city = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    