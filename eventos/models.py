from django.db import models

# Create your models here.
from colaborador.models import Colaborador


class Eventos(models.Model):
    nome = models.CharField(max_length=255)
    local = models.CharField(max_length=255)
    data = models.CharField(max_length=255)
    hora = models.CharField(max_length=255)
    participantes = models.CharField(max_length=255)
    organizador = models.ForeignKey(
        Colaborador,
        on_delete=models.SET_NULL,
        null=True
    )



