from core.models import Pessoa
from monografia.models import Monografia
from rest_framework import serializers


class PessoaSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Pessoa
        fields = ['nome', 'email']

class MonografiaSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Monografia
        fields = ['titulo', 'autor']