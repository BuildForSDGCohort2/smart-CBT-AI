from django.db import models
from django.db.models import CharField, TextField, Model
from django_mysql.models import ListCharField
from django_mysql.models import ListTextField



# Create your models here.
class Objective(models.Model):

    question = models.CharField(max_length = 200, null=True) #questions to be answered
    options = ListCharField(base_field=CharField(max_length=100), size=4, max_length=(4*101), null=True)
    solution = models.CharField(max_length = 100, null=True) #students' answer
    answer = models.CharField(max_length =100, null=True) #teacher's answer
    
    def __str__(self):
        return self.question

class Theory(models.Model):
    question = models.CharField(max_length = 300, null=True) #questions to be answered
    solution = models.TextField(null=True)  #students' answer
    answer = ListTextField(CharField(max_length = 500), size=3, max_length = 501*3, null=True) #teacher's answer

    def __str__(self):
        return self.question
