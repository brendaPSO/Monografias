from turtle import title

import django_filters
from .models import Monografia
from core.models import Pessoa

class MonografiaFilter(django_filters.FilterSet):
    titulo = django_filters.CharFilter(lookup_expr='icontains', label='Título')
    autor__nome = django_filters.CharFilter(lookup_expr='icontains', label='Autor')
    orientador__nome = django_filters.CharFilter(lookup_expr='icontains', label='Orientador')
    coorientador__nome = django_filters.CharFilter(lookup_expr='icontains', label='Coorientador')
    resumo = django_filters.CharFilter(lookup_expr='icontains', label='Resumo')
    palavrachave = django_filters.CharFilter(lookup_expr='icontains', label='Palavra-Chave')
    universidade = django_filters.CharFilter(lookup_expr='icontains', label='Universidade')
    curso = django_filters.CharFilter(lookup_expr='icontains', label='Curso')

    class Meta:
        model = Monografia
        fields = ('titulo','autor__nome', 'orientador__nome', 'coorientador__nome', 'resumo', 'palavrachave', 'universidade', 'curso')
