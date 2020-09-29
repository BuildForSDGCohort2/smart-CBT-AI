# serializers.py
from rest_framework import serializers

from .models import Theory


class TheorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Theory
        fields = ('id', 'question', 'solution', 'answer')
        