from django.db import models

# Create your models here.
class Monografia (models.Model):
    titulo = models.CharField(max_length=200, default = "")
    autor = models.CharField(max_length=100, default = "")
    orientador = models.CharField(max_length=100, default = "")
    coorientador = models.CharField(max_length=100, default = "")
    data = models.CharField(max_length=50, default = "")
    resumo = models.CharField(max_length=250, default = "")
    palavrachave = models.CharField("Palavra-chave", max_length=200, default = "")
    universidade = models.CharField(max_length=100, default = "")
    curso = models.CharField(max_length=100, default = "")
    link = models.CharField("Link para PDF", max_length=300, default = "")

    def __str__(self):
        return self.nome
