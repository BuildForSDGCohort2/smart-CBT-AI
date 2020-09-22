# serializers.py
from rest_framework import serializers

from .models import Objective
from .models import Theory

class ObjectiveSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Objective
        fields = ('id', 'question', 'options', 'solution', 'answer')

class TheorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Theory
        fields = ('id', 'question', 'solution', 'answer')
        