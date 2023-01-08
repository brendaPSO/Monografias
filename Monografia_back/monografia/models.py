from django.db import models
from core.models import Pessoa

# Create your models here.
class Monografia (models.Model):
    titulo = models.CharField(max_length=256, default = "")
    autor = models.OneToOneField(Pessoa, on_delete=models.CASCADE, related_name='autor', blank=True)
    orientador = models.ForeignKey(Pessoa, on_delete=models.CASCADE, related_name='orientador',blank=True)
    coorientador = models.ForeignKey(Pessoa, on_delete=models.CASCADE, related_name='coorientador',blank=True)
    data = models.DateField(max_length=30, default = "")
    resumo = models.TextField(max_length=3200, default = "")
    palavrachave = models.CharField("Palavra-chave", max_length=100, default = "")
    universidade = models.CharField(max_length=128, default = "")
    curso = models.CharField(max_length=100, default = "")
    link = models.URLField("Link para PDF", max_length=512, default = "")

    def __str__(self):
        return self.titulo
