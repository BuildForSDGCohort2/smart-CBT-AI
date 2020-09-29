from django.db import models
from django.db.models import CharField, TextField, Model
from django_mysql.models import ListCharField
from django_mysql.models import ListTextField
from cbtapi.models import Theory

# Create your models here.

class Result_Theory(models.Model):
    question = models.ForeignKey(to=Theory, on_delete=models.CASCADE, null=True)
    score = models.IntegerField()

    def __int__(self):
        return self.question

class Result(models.Model):
    score = models.IntegerField()

    def __int__(self):
        return self.question