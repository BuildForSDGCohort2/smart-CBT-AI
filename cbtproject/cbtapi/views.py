from django.shortcuts import render
from rest_framework import viewsets
from django.http import HttpResponse
from .serializers import ObjectiveSerializer
from .serializers import TheorySerializer
from .models import Objective
from .models import Theory

# Create your views here.

class ObjectiveViewSet(viewsets.ModelViewSet):
    queryset = Objective.objects.all().order_by('question')
    serializer_class = ObjectiveSerializer

class TheoryViewSet(viewsets.ModelViewSet):
    queryset = Theory.objects.all().order_by('question')
    serializer_class = TheorySerializer
