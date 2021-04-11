from django.forms import ModelForm
from .models import Student,Category,EvidenceRec,Additional,Task,Studentgrades
from django import forms

from .models import EvidenceRec


class StudentForm(ModelForm):
    class Meta:
        model=Student
        fields=('first_name','last_name','semester','grade','class_name',)
        labels={
            'first_name':'First Name',
            'last_name':'Last Name',
            'semester':'Semester',
            'class_name':'Class Name',
        }
    
class CategoryForm(ModelForm):
    class Meta:
        model=Category
        fields=('category_name',)
        labels={
            'category_name':'Category Name',
        }
            
class AdditionalForm(ModelForm):
    class Meta:
        model=Additional
        fields=('comments','final_grade',)
        labels={
            'final_grade':'Final Grade',
            'comments': 'Comments,'
        }
class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ('name','class_code','date',)
        labels = {
            'name': 'Task Name',
            'class_code': 'Class Code'
        }

class Studentgradesform(ModelForm):
     class Meta:
         model=Studentgrades
         fields=('first_name','last_name','class_name',)
         labels={
            'first_name':'First Name',
            'last_name':'Last Name',
            'class_name':'Class Name',
        }


class EviForm(ModelForm):
    class Meta:
         model = EvidenceRec
         fields = ('__all__')
         labels = {
            'inc': 'INC',
            'r_minus': 'R-',
            'r_middle': 'R',
            'r_plus': 'R+',
            'one_minus': '1-',
            'one_middle': '1',
            'one_plus': '1+',
            'two_minus': '2-',
            'two_middle': '2',
            'two_plus': '2+',
            'three_minus':'3-',
            'three_middle':'3',
            'three_plus':'3+',
            'threepfourm':'3+/4-',
            'four_minus':'4-',
            'fourmfourmid':'4-/4',
            'four_middle':'4',
            'fourmfourp':'4/4+',
            'four_plus':'4+',
            'four_plusplus':'4++',

        }
    
class Categoryform(ModelForm):
     class Meta:
         model = Category
         fields = ('__all__')

class Additionalform(ModelForm):
    class Meta:
         model = Additional
         fields = ('__all__')
         labels = {
            'comments': 'Comments',
            'final_grade': 'Final Grade',
         }

