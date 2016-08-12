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
    created_date = models.DateTimeField(
            default=timezone.now)
    update_date = models.DateTimeField(
            default=timezone.now)

    def __str__(self):
        return self.nome

class Curso(models.Model):
    nome = models.CharField(max_length=300)
    instituicao = models.ForeignKey('Instituicao')
    created_date = models.DateTimeField(
            default=timezone.now)
    update_date = models.DateTimeField(
            default=timezone.now)

    def __str__(self):
        return self.nome

class Disciplina(models.Model):
    nome = models.CharField(max_length=300)
    curso = models.ForeignKey('Curso')
    created_date = models.DateTimeField(
            default=timezone.now)
    update_date = models.DateTimeField(
            default=timezone.now)

    def __str__(self):
        return self.nome

class Aula(models.Model):
    nome = models.CharField(max_length=300)
    disciplina = models.ForeignKey('Disciplina')
    aula_date = models.DateTimeField(
            default=timezone.now)
    update_date = models.DateTimeField(
            default=timezone.now)
    execucao_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.execucao_date = timezone.now()
        self.save()

    def __str__(self):
        return self.nome

class Perfil(models.Model):
    nome = models.CharField(max_length=300)
    created_date = models.DateTimeField(
            default=timezone.now)
    update_date = models.DateTimeField(
            default=timezone.now)

    def __str__(self):
        return self.nome

class Usuario(models.Model):
    nome = models.CharField(max_length=300)
    email = models.CharField(max_length=300)
    telefone = models.CharField(max_length=300)
    perfil = models.ForeignKey('Perfil')
    instituicao = models.ForeignKey('Instituicao')
    created_date = models.DateTimeField(
            default=timezone.now)
    update_date = models.DateTimeField(
            default=timezone.now)

    def __str__(self):
        return self.nome