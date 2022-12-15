from core.models import Pessoa
from rest_framework import viewsets
from .serializers import PessoaSerializers, MonografiaSerializers
from monografia.models import Monografia

class PessoaViewSet(viewsets.ModelViewSet):
    """
    API endpoint que permite adcionar ou editar pessoas.
    """
    queryset = Pessoa.objects.all()
    serializer_class = PessoaSerializers

class MonografiaViewSet(viewsets.ModelViewSet):
    """
    API endpoint que permite adcionar ou editar Monografias.
    """
    queryset = Monografia.objects.all()
    serializer_class = MonografiaSerializers