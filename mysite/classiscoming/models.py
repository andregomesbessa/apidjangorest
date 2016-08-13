from django.db import models
from django.utils import timezone #Adicionado
from django.contrib.auth.models import User

# Create your models here.
class Instituicao(models.Model):
    nome = models.CharField(max_length=300)
    sigla = models.CharField(max_length=300)
    cidade = models.CharField(max_length=300)
    estado = models.CharField(max_length=300)
    pais = models.CharField(max_length=300)

    def __str__(self):
        return self.nome

class Curso(models.Model):
    nome = models.CharField(max_length=300)
    created_date = models.DateTimeField(
            default=timezone.now)
    update_date = models.DateTimeField(
            default=timezone.now)

    def __str__(self):
        return self.nome

class InstituicaoCurso(models.Model):
    curso = models.ForeignKey('Curso')
    instituicao = models.ForeignKey('Instituicao')
    created_date = models.DateTimeField(
            default=timezone.now)
    update_date = models.DateTimeField(
            default=timezone.now)

    def __str__(self):
        return self.instituicao.sigla + " - " + self.curso.nome

class TipoEvento(models.Model):
    nome = models.CharField(max_length=300)
    descricao = models.CharField(max_length=300)
    created_date = models.DateTimeField(
            default=timezone.now)
    update_date = models.DateTimeField(
            default=timezone.now)

    def __str__(self):
        return self.nome

class Evento(models.Model):
    nome = models.CharField(max_length=300)
    tipoEvento = models.ForeignKey('TipoEvento')
    instituicao = models.ForeignKey('Instituicao')
    inicio_date = models.DateTimeField(
            default=timezone.now)
    fim_date = models.DateTimeField(
            default=timezone.now)
    created_date = models.DateTimeField(
            default=timezone.now)
    update_date = models.DateTimeField(
            default=timezone.now)

    def __str__(self):
        return self.nome

class CursoEvento(models.Model):
    evento = models.ForeignKey('Evento')
    curso = models.ForeignKey('Curso')
    created_date = models.DateTimeField(
            default=timezone.now)
    update_date = models.DateTimeField(
            default=timezone.now)

    def __str__(self):
        return self.curso.nome + " - " + self.evento.nome

class OcorrenciaEvento(models.Model):
    evento = models.ForeignKey('Evento')
    nome = models.CharField(max_length=300)
    ocorrencia_inicio_date = models.DateTimeField(
            default=timezone.now)
    ocorrencia_fim_date = models.DateTimeField(
            default=timezone.now)
    update_date = models.DateTimeField(
            default=timezone.now)

    def __str__(self):
        return self.nome

class TipoUsuario(models.Model):
    nome = models.CharField(max_length=300)
    descricao = models.CharField(max_length=300)
    created_date = models.DateTimeField(
            default=timezone.now)
    update_date = models.DateTimeField(
            default=timezone.now)

    def __str__(self):
        return self.nome

class Usuario(models.Model):
    usuario = models.ForeignKey('auth.User')
    tipoUsuario = models.ForeignKey('TipoUsuario')
    nome = models.CharField(max_length=300)
    email = models.CharField(max_length=300)
    telefone = models.CharField(max_length=300)
    created_date = models.DateTimeField(
            default=timezone.now)
    update_date = models.DateTimeField(
            default=timezone.now)

    def __str__(self):
        return self.nome

class UsuarioInstituicao(models.Model):
    usuario = models.ForeignKey('Usuario')
    instituicao = models.ForeignKey('Instituicao')
    created_date = models.DateTimeField(
            default=timezone.now)
    update_date = models.DateTimeField(
            default=timezone.now)

    def __str__(self):
        return self.instituicao.sigla + " - " + self.usuario.nome 

class UsuarioEvento(models.Model):
    evento = models.ForeignKey('Evento')
    usuario = models.ForeignKey('Usuario')
    created_date = models.DateTimeField(
            default=timezone.now)
    update_date = models.DateTimeField(
            default=timezone.now)

    def __str__(self):
        return self.evento.nome + " - " + self.usuario.nome

class FaltaOcorrenciaEvento(models.Model):
    ocorrenciaEvento = models.ForeignKey('OcorrenciaEvento')
    usuario = models.ForeignKey('Usuario')
    created_date = models.DateTimeField(
            default=timezone.now)
    update_date = models.DateTimeField(
            default=timezone.now)

    def __str__(self):
        return self.nome