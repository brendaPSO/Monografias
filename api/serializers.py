from core.models import Pessoa
from monografia.models import Monografia
from rest_framework import serializers

class PessoaSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Pessoa
        fields = ['id', 'nome', 'tipo', 'curso', 'universidade', 'email', 'curriculo', 'google_scholar', 'research_gate', 'linkedin', 'orcid', 'github']

class MonografiaSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Monografia
        fields = ['id', 'titulo', 'autor', 'orientador', 'coorientador', 'data', 'resumo', 'palavrachave', 'universidade', 'curso', 'link']