from django.contrib import admin

#Imports the models to the Django admin page
from .models import *

admin.site.register(Student)
admin.site.register(Studentgrades)
admin.site.register(Task)
admin.site.register(EvidenceRec)
admin.site.register(Category)
admin.site.register(Additional)

