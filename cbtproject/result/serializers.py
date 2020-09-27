# serializers.py
from rest_framework import serializers

from .models import Result_Obj
from .models import Result_Theory
from .models import Result

class Result_ObjSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Result_Obj
        fields = ('question_id', 'score', 'question')

class Result_TheorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Result_Theory
        fields = ('question_id', 'score', 'question')

class ResultSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Result
        fields = ('id', 'score')