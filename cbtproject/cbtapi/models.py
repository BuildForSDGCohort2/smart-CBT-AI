from django.db import models
from django.db.models import CharField, TextField, Model
from django_mysql.models import ListCharField
from django_mysql.models import ListTextField



# Create your models here.
class Objective(models.Model):

    question = models.CharField(max_length = 60, null=False) #questions to be answered
    options = ListCharField(base_field=CharField(max_length=30), size=4, max_length=(4*31), null=False)
    solution = models.CharField(max_length = 10, null=True) #students' answer
    answer = models.CharField(max_length =10, null=False) #teacher's answer
    
    def __str__(self):
        return self.question

class Theory(models.Model):
    question = models.CharField(max_length = 60, null=False) #questions to be answered
    solution = models.TextField(max_length = 10, null=True)  #students' answer
    answer = ListTextField(base_field=CharField(max_length = 60), size=3, null=False) #teacher's answer

    def __str__(self):
        return self.question
