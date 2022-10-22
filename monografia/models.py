from django.db import models

# Create your models here.
class Monografia (models.Model):
    titulo = models.CharField(max_length=256, default = "")
    autor = models.CharField(max_length=80, default = "")
    orientador = models.CharField(max_length=80, default = "")
    coorientador = models.CharField(max_length=80, default = "")
    data = models.DateField(max_length=30, default = "")
    resumo = models.TextField(max_length=3200, default = "")
    palavrachave = models.CharField("Palavra-chave", max_length=100, default = "")
    universidade = models.CharField(max_length=128, default = "")
    curso = models.CharField(max_length=100, default = "")
    link = models.CharField("Link para PDF", max_length=512, default = "")

    def __str__(self):
        return self.nome
