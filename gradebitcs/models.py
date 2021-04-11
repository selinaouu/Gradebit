from django.db import models

# Create your models here.

class Desination(models.Model):
    first_name=models.TextField()
    last_name=models.TextField()
    grade=models.IntegerField()
    classs=models.CharField()
    semester=models.IntegerField()
