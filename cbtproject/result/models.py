from django.db import models
from django.db.models import CharField, TextField, Model
from django_mysql.models import ListCharField
from django_mysql.models import ListTextField
from cbtapi.models import Objective, Theory

# Create your models here.
class Result_Obj(models.Model):
    score = models.IntegerField()
    question = models.ForeignKey(to=Objective, on_delete=models.CASCADE, null=True)
    isCorrect = models.BooleanField()

    def __str__(self):
        return self.score

class Result_Theory(models.Model):
    score = models.IntegerField()
    question = models.ForeignKey(to=Theory, on_delete=models.CASCADE, null=True)
    isCorrect = models.BooleanField()

    def __str__(self):
        return self.score

class Result(models.Model):
    score = models.IntegerField()

    def __str__(self):
        return self.score