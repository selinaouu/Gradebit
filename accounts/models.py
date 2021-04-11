from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User

 #create models that connect the the db and creates tables in the db

class Student(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="new_spending", null=True)   
    first_name=models.CharField(max_length=30)
    last_name=models.CharField(max_length=30)
    semester=models.PositiveIntegerField()
    grade=models.PositiveIntegerField()
    class_name=models.CharField(max_length=20)

class Studentgrades(models.Model):
    user= models.ForeignKey(User, on_delete=models.CASCADE, related_name="new_studentgrades", null=True)   
    first_name=models.CharField(max_length=30)
    last_name=models.CharField(max_length=30)
    class_name=models.CharField(max_length=20)

class Additional(models.Model):
    studentgrades= models.ForeignKey(Studentgrades, on_delete=models.SET_NULL,null=True)   
    comments=models.CharField(max_length=200)
    final_grade=models.IntegerField()

class Task(models.Model):
    user= models.ForeignKey(User, on_delete=models.CASCADE, related_name="new_task", null=True)   
    name = models.CharField(max_length=75)
    class_code = models.CharField(max_length=10)
    date = models.CharField(max_length=10)
            
class EvidenceRec(models.Model):
    studentgrades= models.ForeignKey(Studentgrades, on_delete=models.SET_NULL,null=True)   
    subcategory=models.CharField(max_length=30)
    inc=models.CharField(max_length=10,blank=True)
    r_minus=models.CharField(max_length=10,blank=True)
    r_middle=models.CharField(max_length=10,blank=True)
    r_plus=models.CharField(max_length=10,blank=True)
    one_minus=models.CharField(max_length=10,blank=True)
    one_middle=models.CharField(max_length=10,blank=True)
    one_plus=models.CharField(max_length=10,blank=True)
    two_minus=models.CharField(max_length=10,blank=True)
    two_middle=models.CharField(max_length=10,blank=True)
    two_plus=models.CharField(max_length=10,blank=True)
    three_minus=models.CharField(max_length=10,blank=True)
    three_middle=models.CharField(max_length=10,blank=True)
    three_plus=models.CharField(max_length=10,blank=True)
    threepfourm=models.CharField(max_length=10,blank=True)
    four_minus=models.CharField(max_length=10,blank=True)
    fourmfourmid=models.CharField(max_length=10,blank=True)
    four_middle=models.CharField(max_length=10,blank=True)
    fourmfourp=models.CharField(max_length=10,blank=True)
    four_plus=models.CharField(max_length=10,blank=True)
    four_plusplus=models.CharField(max_length=10,blank=True)
    level=models.CharField(max_length=10,blank=True)
    expectation = models.CharField(max_length= 170,null=True)

class Category(models.Model):
    studentgrades= models.ForeignKey(Studentgrades, on_delete=models.SET_NULL,null=True)   
    category_name=models.CharField(max_length=70)