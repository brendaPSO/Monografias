from django.db import models


class Pessoa(models.Model):
    TIPO_PESSOAS = (
        ('1', 'Autor'),
        ('2', 'Orientador'),
        ('3', 'Coorientador'),
    )

    nome = models.CharField(max_length=80, null=True , blank=True)
    tipo = models.CharField(max_length=30, choices=TIPO_PESSOAS)
    curso = models.CharField(max_length=100, default='')
    universidade = models.CharField(max_length=128, default='')
    email = models.EmailField(max_length=256, unique=True, default='')
    curriculo = models.URLField(max_length=512, null=True, blank=True)
    google_scholar = models.URLField(max_length=512, null=True, blank=True)
    research_gate = models.URLField(max_length=512, null=True, blank=True)
    linkedin = models.URLField(max_length=512, null=True, blank=True)
    orcid = models.URLField(max_length=512, null=True, blank=True)
    github = models.URLField(max_length=512, null=True, blank=True)

    def __str__(self):
        return self.nome
