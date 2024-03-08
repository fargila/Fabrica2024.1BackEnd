from rest_framework.serializers import ModelSerializer
from ..models import PessoaDB

class PessoaSerializer(ModelSerializer):
    class Meta:
        model = PessoaDB
        fields = ['id', 'primeiro_nome', 'segundo_nome', 'idade']