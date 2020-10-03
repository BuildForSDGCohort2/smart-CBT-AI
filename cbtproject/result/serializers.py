# serializers.py
from rest_framework import serializers

from .models import Result_Theory
from .models import Result


class Result_TheorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Result_Theory
        fields = ('questionId', 'score')

class ResultSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Result
        fields = ('score')