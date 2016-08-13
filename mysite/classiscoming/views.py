from rest_framework import mixins
from rest_framework import generics
from rest_framework import viewsets

from django.shortcuts import render
from django.utils import timezone
from .models import Aula, Disciplina

from django.contrib.auth.models import User, Group
from classiscoming.serializers import AulaSerializer, DisciplinaSerializer

# Create your views here.
class DisciplinaViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Disciplina.objects.all()
    serializer_class = DisciplinaSerializer


class AulaViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Aula.objects.all()
    serializer_class = AulaSerializer

