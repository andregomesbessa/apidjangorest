from rest_framework import mixins
from rest_framework import generics
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view

from django.shortcuts import render
from django.utils import timezone
from .models import Instituicao, Curso, InstituicaoCurso, TipoEvento, Evento, CursoEvento, OcorrenciaEvento, TipoUsuario, Usuario, UsuarioInstituicao, UsuarioEvento, FaltaOcorrenciaEvento

from django.contrib.auth.models import User, Group
from classiscoming.serializers import InstituicaoSerializer, CursoSerializer, TipoEventoSerializer, EventoSerializer, TipoUsuarioSerializer, UsuarioEventoSerializer, UsuarioSerializer, ParticipantesEventoSerializer 

# Create your views here.
class InstituicaoViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Instituicao.objects.all()
    serializer_class = InstituicaoSerializer


class CursoViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer

class TipoEventoViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = TipoEvento.objects.all()
    serializer_class = TipoEventoSerializer

class EventoViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Evento.objects.all()
    serializer_class = EventoSerializer

class TipoUsuarioViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = TipoUsuario.objects.all()
    serializer_class = TipoUsuarioSerializer

class UsuarioViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

class UsuarioEventoViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = UsuarioEvento.objects.all()
    serializer_class = UsuarioEventoSerializer

@api_view(['GET'])
def obter_eventos_usuario(request, usuario):
    try:
        result = UsuarioEvento.objects.filter(usuario=usuario)
        usuarioevento = list(result)
    except UsuarioEvento.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = UsuarioEventoSerializer(usuarioevento, context={'request': request}, many=True)        
        return Response(serializer.data)

@api_view(['GET'])
def obter_participantes_evento(request, evento):
    try:
        result = UsuarioEvento.objects.filter(evento=evento)
        usuarioevento = list(result)

    except UsuarioEvento.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = ParticipantesEventoSerializer(usuarioevento, context={'request': request}, many=True)        
        return Response(serializer.data)