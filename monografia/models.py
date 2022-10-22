from django.db import models

# Create your models here.
class Monografia (models.Model):
    nome = models.CharField(max_length=200, default = "")
    titulo = models.CharField(max_length=30, default = "")
    autor = models.CharField(max_length=31, default = "")
    orientador = models.CharField(max_length=33, default = "")
    coorientador = models.CharField(max_length=35, default = "")
    data = models.CharField(max_length=30, default = "")
    resumo = models.CharField(max_length=30, default = "")
    palavrachave = models.CharField("Palavra-chave", max_length=30, default = "")
    universidade = models.CharField(max_length=30, default = "")
    curso = models.CharField(max_length=50, default = "")
    link = models.CharField("Link para PDF", max_length=200, default = "")

    def __str__(self):
        return self.nome