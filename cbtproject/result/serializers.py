# serializers.py
from rest_framework import serializers

from .models import Result_Obj
from .models import Result_Theory

class Result_ObjSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Result_Obj
        fields = ('id', 'score', 'question', 'isCorrect')

class Result_TheorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Result_Theory
        fields = ('id', 'score', 'question', 'isCorrect')
