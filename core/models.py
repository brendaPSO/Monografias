from django.db import models


class Pessoa(models.Model):
    TIPO_PESSOAS = (
        (1, 'Autor'),
        (2, 'Coautor'),
        (3, 'Discentes'),
    )

    nome = models.CharField(max_length=100, default='')
    tipo = models.CharField(max_length=1, choices=TIPO_PESSOAS, default=1)
    curso = models.CharField(max_length=100, default='')
    universidade = models.CharField(max_length=128, default='')
    email = models.EmailField(max_length=254, unique=True, default='')
    curriculo = models.URLField(max_length=128, null=True, blank=True)
    google_scholar = models.URLField(max_length=128, null=True, blank=True)
    research_gate = models.URLField(max_length=128, null=True, blank=True)
    linkedin = models.URLField(max_length=128, null=True, blank=True)
    orcid = models.URLField(max_length=128, null=True, blank=True)
    github = models.URLField(max_length=128, null=True, blank=True)

    def __str__(self):
        return self.nome
