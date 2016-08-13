from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Aula, Disciplina


class DisciplinaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Disciplina
        fields = ('id','nome', 'created_date', 'update_date')

class AulaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Aula
        fields = ('id', 'nome', 'disciplina', 'aula_date', 'update_date', 'execucao_date')
 