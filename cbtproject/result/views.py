from django.shortcuts import render
from rest_framework import viewsets

from .serializers import Result_TheorySerializer, ResultSerializer
from .models import Result_Theory, Result

# Create your views here.

class Result_TheoryViewSet(viewsets.ModelViewSet):
    queryset = Result_Theory.objects.all().order_by('questionId')
    serializer_class = Result_TheorySerializer

class ResultViewSet(viewsets.ModelViewSet):
    queryset = Result.objects.all().order_by('score')
    serializer_class = ResultSerializer