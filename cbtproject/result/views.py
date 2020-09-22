from django.shortcuts import render
from rest_framework import viewsets

from .serializers import Result_ObjSerializer, Result_TheorySerializer
from .models import Result_Obj, Result_Theory

# Create your views here.
class Result_ObjViewSet(viewsets.ModelViewSet):
    queryset = Result_Obj.objects.all().order_by('question')
    serializer_class = Result_ObjSerializer

class Result_TheoryViewSet(viewsets.ModelViewSet):
    queryset = Result_Theory.objects.all().order_by('question')
    serializer_class = Result_TheorySerializer