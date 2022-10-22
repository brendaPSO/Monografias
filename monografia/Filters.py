from turtle import title

import django_filters
from .models import Monografia

class MonografiaFilter(django_filters.FilterSet):
    titulo = django_filters.CharFilter(lookup_expr='icontains', label='Título')
    autor = django_filters.CharFilter(lookup_expr='icontains', label='Autor')
    orientador = django_filters.CharFilter(lookup_expr='icontains', label='Orientador')
    coorientador = django_filters.CharFilter(lookup_expr='icontains', label='Coorientador')
    resumo = django_filters.CharFilter(lookup_expr='icontains', label='Resumo')
    palavrachave = django_filters.CharFilter(lookup_expr='icontains', label='Palavra-Chave')
    universidade = django_filters.CharFilter(lookup_expr='icontains', label='Universidade')
    curso = django_filters.CharFilter(lookup_expr='icontains', label='Curso')

    class Meta:
        model = Monografia
        fields = ('titulo','autor', 'orientador', 'coorientador', 'resumo', 'palavrachave', 'universidade', 'curso')
