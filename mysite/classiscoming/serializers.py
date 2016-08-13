from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Curso, Evento, TipoEvento, Instituicao, TipoUsuario, Usuario, UsuarioEvento 

class InstituicaoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Instituicao
        fields = ('id','nome')

class CursoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Curso
        fields = ('id','nome')

class TipoEventoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TipoEvento
        fields = ('id', 'nome', 'descricao')

class EventoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Evento
        fields = ('id', 'nome', 'tipoEvento', 'instituicao', 'inicio_date','fim_date')

class TipoUsuarioSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TipoUsuario
        fields = ('id', 'nome', 'descricao')

class UsuarioSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Usuario
        fields = ('id', 'nome', 'tipoUsuario', 'email')

class UsuarioEventoSerializer(serializers.ModelSerializer):
    class Meta:
        model = UsuarioEvento
        fields = ('id', 'evento', 'usuario')
 