from django.db import models
from django.db.models import CharField, TextField, Model
from django_mysql.models import ListCharField
from django_mysql.models import ListTextField

# Create your models here.

class Result_Theory(models.Model):
    questionId = models.IntegerField()
    score = models.IntegerField()

    def __int__(self):
        return self.question

class Result(models.Model):
    score = models.IntegerField()

    def __int__(self):
        return self.question