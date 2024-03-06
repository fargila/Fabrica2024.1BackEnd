from rest_framework.viewsets import ModelViewSet
from ..models import PessoaDB
from .serializers import PessoaSerializer

class PessoaViewSet(ModelViewSet):
    serializer_class = PessoaSerializer
    queryset = PessoaDB.objects.all()