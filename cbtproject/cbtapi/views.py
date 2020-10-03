from django.shortcuts import render
from rest_framework import viewsets
from django.http import HttpResponse
from .serializers import TheorySerializer
from .models import Theory

# Create your views here.


class TheoryViewSet(viewsets.ModelViewSet):
    queryset = Theory.objects.all().order_by('question')
    serializer_class = TheorySerializer
