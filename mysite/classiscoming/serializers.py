from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Curso, Evento, TipoEvento, Instituicao, TipoUsuario, Usuario, UsuarioEvento, OcorrenciaEvento, FaltaOcorrenciaEvento 

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
        fields = ('id', 'nome', 'inicio_date','fim_date')

class TipoUsuarioSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TipoUsuario
        fields = ('id', 'nome', 'descricao')

class UsuarioSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Usuario
        fields = ('id', 'nome', 'tipoUsuario', 'email')

class UsuarioEventoSerializer(serializers.HyperlinkedModelSerializer):
    usuario = UsuarioSerializer(many=False, read_only=True)
    evento = EventoSerializer(many=False, read_only=True)
    class Meta:
        model = UsuarioEvento
        fields = ('id','evento','usuario')

class EventosUsuarioSerializer(serializers.HyperlinkedModelSerializer):
    evento = EventoSerializer(many=False, read_only=True)
    class Meta:
        model = UsuarioEvento
        fields = ('evento',)

class ParticipantesEventoSerializer(serializers.HyperlinkedModelSerializer):
    usuario = UsuarioSerializer(many=False, read_only=True)
    class Meta:
        model = UsuarioEvento
        fields = ('usuario',)

class OcorrenciaEventoSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = OcorrenciaEvento
        fields = ('id', 'nome', 'ocorrencia_inicio_date', 'ocorrencia_fim_date')

class FaltaOcorrenciaEventoSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = FaltaOcorrenciaEvento
        fields = ('id', 'ocorrenciaEvento', 'usuario')

        